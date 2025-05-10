from app.db import engine, SessionLocal
from app.models import SlowQuery, LongTransactions
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def get_slow_queries():
    try:
        with engine.connect() as conn:
            query = '''
                SELECT sql_id, elapsed_time, sql_text
                FROM v$sql
                WHERE elapsed_time > 1000000
                ORDER BY elapsed_time DESC FETCH FIRST 10 ROWS ONLY
            '''
            result = conn.execute(query)

            db = SessionLocal()
            response = []

            for row in result:
                sql_id, elapsed_time, sql_text = row
                record = SlowQuery(
                    sql_id=sql_id,
                    elapsed_time=elapsed_time,
                    sql_text=sql_text
                )
                db.add(record)
                response.append({
                    "sql_id": sql_id,
                    "elapsed_time": elapsed_time,
                    "sql_text": sql_text
                })

            db.commit()
            db.close()

            logger.info(f"Collected and stored {len(response)} slow queries.")
            return response

    except Exception as e:
        logger.error(f"Failed to get slow queries: {str(e)}")
        return {"error": str(e)}

def get_long_running_transactions():
    try:
        with engine.connect() as conn:
            query = '''
                SELECT s.sid, s.serial#, s.username, t.start_time
                FROM v$transaction t
                JOIN v$session s ON t.ses_addr = s.saddr
                WHERE t.start_time < SYSDATE - (1/24/60)  -- 1 minute
            '''
            result = conn.execute(query)

            db = SessionLocal()
            response = []

            for row in result:
                sid, serial, username, start_time = row
                record = LongTransactions(
                    sid=sid,
                    serial=serial,
                    username=username,
                    start_time=start_time
                )
                db.add(record)
                response.append({
                    "sid": sid,
                    "serial": serial,
                    "username": username,
                    "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S") if isinstance(start_time, datetime) else str(start_time)
                })

            db.commit()
            db.close()

            logger.info(f"Stored {len(response)} long-running transactions.")
            return response

    except Exception as e:
        logger.error(f"Failed to get long running transactions: {str(e)}")
        return {"error": str(e)}
