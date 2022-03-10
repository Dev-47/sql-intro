import psycopg2
import time

db_configs = {
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5433",
}


def log(message):
    print(message)


def execute_query(query):
    log("*" * 30)

    start = time.perf_counter()

    connection = psycopg2.connect(**db_configs)

    log("connecting to database ...")
    cursor = connection.cursor()
    log("database connected !")

    log("executing query ...")
    cursor.execute(query)
    log("query executed !")

    log("committing query ...")
    connection.commit()
    log("query commited !")

    try:
        query_result = cursor.fetchall()
    except Exception:
        query_result = None

    connection.close()
    log("connection closed !")

    end = time.perf_counter()

    log("*" * 30)
    log("query took %ss to run" % round(end - start, 2))

    return query_result
