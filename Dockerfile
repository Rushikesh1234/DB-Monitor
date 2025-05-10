FROM python:3.10

RUN apt-get update && \
    apt-get install -y libaio1 unzip curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L -o instantclient-basic.zip https://download.oracle.com/otn_software/linux/instantclient/2380000/instantclient-basic-linux.x64-23.8.0.25.04.zip && \
    unzip instantclient-basic.zip && \
    mkdir -p /opt/oracle && \
    mv instantclient_23_8 /opt/oracle/instantclient && \
    rm instantclient-basic.zip

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
ENV PATH=$ORACLE_HOME:$PATH

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
