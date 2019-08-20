from flask import Flask
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url, URL
import pandas as pd

app = Flask(__name__)

WELCOME_TEXT = os.environ["WELCOME_TEXT"]
CLOUD_SQL_URI = os.environ["CLOUD_SQL_URI"]
CLOUD_SQL_PASSWORD = os.environ["CLOUD_SQL_PASSWORD"]


# CLOUD_SQL_URI = "mysql://root@10.114.193.5:3306/mysql"
# CLOUD_SQL_URI = "mysql://root@127.0.0.1:3307/mysql"
# CLOUD_SQL_PASSWORD = "xxrDqEIK103wxtPu"


class SqlRunner:

    def __init__(self, uri, password):
        self.uri = uri
        self.password = password

    @staticmethod
    def get_connection_url(db_uri, password):
        url = make_url(db_uri)
        connection_url = URL(url.drivername, url.username, password, url.host, url.port, url.database, {})
        return connection_url

    def run_query(self, sql_query, result_size=50):
        print("Running Query => {}".format(sql_query))
        connection_url = SqlRunner.get_connection_url(self.uri, self.password)
        engine = create_engine(connection_url, echo=False)
        query_results = pd.read_sql_query(sql_query, engine, chunksize=result_size)
        return query_results

    def get_mysql_users(self):
        all_users = []
        sql_query = "SELECT User FROM mysql.user"
        query_results = self.run_query(sql_query)
        for users in query_results:
            users_array = users['User'].get_values()
            for user in users_array:
                all_users.append(user)

        return all_users


@app.route("/")
def hello():
    all_users = SqlRunner(CLOUD_SQL_URI, CLOUD_SQL_PASSWORD).get_mysql_users()
    html = "<h1 style='text-align:center;margin:20px;'>Greetings from " + WELCOME_TEXT + "</h1>"
    html = html + "</br> <h2 style='text-align:center;margin:20px;'>These are the users available in the database => " + ', '.join(
        all_users) + "</h2>"
    return html


@app.route("/heartbeat")
def healthcheck():
    html = "<h1 style='text-align:center;margin:20px;'>M Alive, yuhooooo</h1>"
    return html


@app.route("/debug")
def debug():
    html = "<h1 style='text-align:center;margin:20px;'>Cloud SQL URI => " + CLOUD_SQL_URI + "</h1>"
    html = html + "</br>" + "<h1 style='text-align:center;margin:20px;'>Cloud SQL PASSWORD => " + CLOUD_SQL_PASSWORD + "</h1>"
    return html


if __name__ == "__main__":
    print("Hello World , M about to start")
    # print("Cloud SQL URI => {}".format(CLOUD_SQL_URI))
    # print("Cloud SQL PASSWORD => {}".format(CLOUD_SQL_PASSWORD))
    app.run(host='0.0.0.0', port=8080)
