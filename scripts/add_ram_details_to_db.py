from hurry.filesize import size
import datetime
from time import sleep
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
import psutil

DEBUG = True
HOST = '0.0.0.0'
PORT = '6500'
MYSQL_HOST = '127.0.0.1'
MYSQL_USERNAME = 'push'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'ram'

migrate = Migrate()
ma = Marshmallow()
db = SQLAlchemy()


def db_connector(db_name=MYSQL_DATABASE):
    try:
        connection = mysql.connector.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USERNAME,
                                             password=MYSQL_PASSWORD,
                                             database=db_name,
                                             connection_timeout=2)
        if connection.is_connected():
            return connection
        else:
            print("can not connect to db")
            raise Exception("can not connect to db")
    except Exception as e:
        print("error in db connection {}".format(e))

        return


def execute_query(query, data=None, connection=None, cursor=None, close_con=True):
    if connection is None and cursor is None:
        connection, cursor = open_db_connection()
    try:
        cursor.execute(query)
    except Exception as e:
        print("error in execute query {}".format(e))
        return

    result = None
    if data is not None:
        if data == "one":
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
    if close_con:
        commit_and_close_db_connection(connection, cursor)
    if result is not None:
        return result


def open_db_connection(db_name=MYSQL_DATABASE):
    connection = db_connector(db_name)
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


def commit_and_close_db_connection(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()


def record_ram_details(used, free, total):
    try:
        time = datetime.datetime.now()
        query = """INSERT INTO ram_usage (used, free, total, time) values ('{}', '{}', '{}', '{}')"""\
            .format(used, free, total, time)
        result = execute_query(query=query, data="all")
    except Exception as e:
        print("error in inserting to db {}".format(e))
        return True
    return result


while True:
    print(">>>>>>>>>>>>>>>>>>>>>>>>> inserting record into db")
    used_ram = size(psutil.virtual_memory()[3])
    free_ram = size(psutil.virtual_memory()[4])
    total_ram = size(psutil.virtual_memory()[0])
    print(free_ram, used_ram, total_ram)
    if total_ram is None:
        print("No data to import")
        sleep(60)
        continue
    else:
        record_ram_details(used_ram, free_ram, total_ram)
        job_time = datetime.datetime.now()
        print("success _ ", job_time)
        sleep(60)
