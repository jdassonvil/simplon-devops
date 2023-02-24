from flask import Flask, redirect, request, url_for, abort
import logging
import psycopg

app = Flask(__name__)

def build_connection_string(pg_host: str):
    # https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    pg_user = "postgres"
    pg_password = "simplon"
    pg_database = "simplon-db"
    return f"postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}"

def read_write_connection():
    return psycopg.connect(build_connection_string("postgres-master"))

def read_only_connection():
    return psycopg.connect(build_connection_string("postgres-replica-1,postgres-replica-2"))


@app.route("/cars")
def list_cars():
    cars = []

    with read_only_connection() as conn:
        cursor = conn.execute("SELECT * FROM cars")
        for record in cursor:
            cars.append({"{} {}".format(record[1], record[2])})

    return "<ul>{}</ul>".format("".join("<li>{}</li>".format(c) for c in cars))


@app.route("/car", methods=["POST"])
def add_car():
    if "maker" not in request.form:
        logging.info("missing maker parameter")
        abort(400) 

    if "model" not in request.form:
        logging.info("missing model parameter")
        abort(400) 

    with read_write_connection() as conn:
        conn.execute("INSERT INTO cars(maker, model) VALUES('{}', '{}')".format(request.form["maker"], request.form["model"]))

    return redirect(url_for("list_cars"))
