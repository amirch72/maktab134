import psycopg2
import logging
import requests
import json

# con = psycopg.connect(
#     database="maktab",
#     user="tamin",
#     password="7294",
#     host="127.0.0.1",
#     port="5432",
# )

# cur = con.cursor()


# if cur:
#     cur.close()
# if con:
#     con.close()

API_ADDRESS = "https://jsonplaceholder.typicode.com/"
DATABASE_NAME = "maktab"
USER = "postgres"
PASSWORD = 7294
HOST = "127.0.0.1"
PORT = 5432


logging.basicConfig(
    level=logging.INFO,
    format="'%(asctime)s - %(name)s | %(levelname)s: %(message)s'",
)
db_logger = logging.getLogger("Database")
data_logger = logging.getLogger("Data")


class PostgresConnetction:
    def __enter__(self):
        db_logger.info("Creating dattabase connection ...")
        self.con = psycopg2.connect(
            database=DATABASE_NAME,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
        )
        # self.con.autocommit = True
        # self.con = con
        self.cur = self.con.cursor()
        db_logger.info("Database connection created successfully!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
        db_logger.info("Database connection closed!")

    def execute(self, query):
        if self.cur:
            db_logger.info("Executing query ...")
            return self.cur.execute(query)
        else:
            db_logger.error("Cursor does not exists!")

    def commit(self):
        if self.con:
            self.con.commit()
            db_logger.info("Data commited!")
        else:
            db_logger.error("Connection does not exists!")

    def fetchall(self):
        return self.cur.fetchall()


with PostgresConnetction() as pgcon:
    data_logger.info("Geting all categories ...")
    query = "select * from category"

    pgcon.execute(query)
    categories = pgcon.fetchall()

    for i in categories:
        print(i[0], i[2])


res = requests.get(f"{API_ADDRESS}users")

with PostgresConnetction() as pgcon:
    for user in res.json():
        get_user_query = f"select * from lecturer where first_name = '{user["name"].split(" ")[0]}' and last_name = '{user["name"].split(" ")[1]}'"
        pgcon.execute(get_user_query)
        all_get_users = pgcon.fetchall()
        if len(all_get_users) > 0:
            data_logger.warning(f"{user["name"]} exists")
        else:
            data_logger.info(f"Adding {user["name"]} to your database ...")
            query = f"insert into lecturer (first_name, last_name, mobile_number, adress, department_id) values('{user["name"].split(" ")[0]}', '{user["name"].split(" ")[1]}', '{user["phone"][:10]}' ,'{user["address"]["street"]}', 3)"
            pgcon.execute(query)
            data_logger.info(f"{user["name"]} added to your database!")
            pgcon.commit()
