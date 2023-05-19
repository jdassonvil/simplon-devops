from flask import Flask, redirect, request, url_for, abort
from datadog import initialize, statsd
import logging
import psycopg
import os

# configure logger
LOG_FORMAT = '%(asctime)s %(message)s'

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
logHandler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(logHandler)

# configure statsd
options = {
    "statsd_host": os.getenv("DD_AGENT_HOST"),
    "statsd_port": 8125,
}
initialize(**options)

app = Flask(__name__)

def db_connection():
    # https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    pg_host = os.getenv("PG_HOST")
    pg_user = os.getenv("PG_USER")
    pg_password = os.getenv("PG_PASSWORD")
    pg_database = os.getenv("PG_DATABASE")
    return psycopg.connect(f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}")

@app.route("/users/<userEmail>")
def get_user(userEmail):
    with db_connection() as conn:
        statsd.increment("demo.users.hits", 1)
        cursor = conn.execute(f"SELECT * FROM users WHERE email='{userEmail}'")

        for record in cursor:
            user = { "id": record[0], "username": record[1], "email": record[2] }
            return user, 200

        return "NOT FOUND", 404
