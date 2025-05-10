<<<<<<< HEAD
# 📦 Database Performance Monitoring and Query Analytics Dashboard (Dockerized)

A lightweight, containerized tool for real-time database performance monitoring and query analytics. Built with FastAPI and Python, it connects to Oracle DB, tracks long-running queries, logs performance metrics, and serves them over RESTful APIs. Visualize data with Grafana or extend it with Prometheus integration.

## 🚀 Features

- 📡 Monitors Oracle DB performance (query time, session state)
- 🌐 REST APIs via FastAPI
- 🗃 Logs slow and long-running queries
- 📈 Compatible with Grafana dashboards
- 🔧 Easily extendable, lightweight design
- 🐳 Runs fully in Docker

## 🛠️ Stack

- FastAPI + Python
- sqlalchemy for Oracle DB connection
- SQLite for storing historical metrics
- Docker for deployment

## 📁 Project Structure

```
db_monitor/
├── app/
│   ├── main.py            # FastAPI routes
│   ├── db.py              # Oracle DB connector
│   ├── metrics.py         # Metrics logic
│   ├── models.py          # SQLite models
│   └── logging.conf       # Logging config
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🐳 Quick Start with Docker

1. Clone the repository:

```bash
git clone https://github.com/yourusername/db-monitor.git
cd db-monitor
```

2. Build the Docker image:

```bash
docker build -t db_monitor .
```

3. Run the container:

```bash
docker run -p 8000:8000 db_monitor
```

The app uses hardcoded Oracle credentials inside db.py for demonstration purposes. No environment variables or additional setup is required.

4. Open API Docs:

```
http://localhost:8000/metrics/slow_queries
http://localhost:8000/metrics/long_transactions
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /metrics/slow_queries | Returns slow SQL queries |
| GET    | /metrics/long_transactions | Returns sessions with long transactions |

## 🧪 Use Cases

- Quick diagnostics of Oracle DB performance
- Prototyping custom metrics exporters
- Hands-on demo for SREs and DBAs

Created for educational and prototyping use. Extend as needed for production.
=======
# db_monitor
>>>>>>> 8a116a234d924a71b2791263c33e07d45101b217
