from fastapi import FastAPI
from app.metrics import get_slow_queries, get_long_running_transactions
import logging
import logging.config
import os
import sys

LOGGING_CONFIG = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOGGING_CONFIG, disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.info("Logger initialized successfully in main.py")

app = FastAPI()

@app.get("/metrics/slow_queries")
def slow_queries():
    logger.info("Endpoint hit: /metrics/slow_queries")
    return get_slow_queries()

@app.get("/metrics/long_transactions")
def long_transactions():
    logger.info("Endpoint hit: /metrics/long_transactions")
    return get_long_running_transactions()
