import argparse

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PostGressArgs:
    def __init__(self, dbName, dbUser, dbPassword, dbHost, dbPort):
        self.Name = dbName
        self.User = dbUser
        self.Password = dbPassword
        self.Host = dbHost
        self.Port = dbPort


def create_database(dbArgs: PostGressArgs):
    dbconnection = psycopg2.connect(
        dbname="postgres",
        user=dbArgs.User,
        host=dbArgs.Host,
        password=dbArgs.Password,
        port=dbArgs.Port,
    )
    dbconnection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    dbcursor = dbconnection.cursor()

    dbcursor.execute(
        f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{dbArgs.Name}'"
    )
    exists = dbcursor.fetchone()
    if not exists:
        query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbArgs.Name))
        dbcursor.execute(query)
        dbconnection.commit()
        print(f"{dbArgs.Name} database created")
    else:
        print(f"{dbArgs.Name} database exists")
        dbcursor.close()
        dbconnection.close()


if __name__ == "__main__":
    parse = argparse.ArgumentParser(
        description="Get the required args creation of reading_db DB"
    )
    parse.add_argument(
        "--dbname",
        help="Name of the database",
        default="reading_db2",
        type=str,
        required=False,
    )
    parse.add_argument(
        "--dbuser", help="Name of the user (e.g postgres)", type=str, required=True
    )
    parse.add_argument(
        "--dbpassword", help="Password of the DB user", type=str, required=True
    )
    parse.add_argument(
        "--dbhost", help="Host url of the postgress instance", type=str, required=True
    )
    parse.add_argument(
        "--dbport",
        help="Port for the postgress instance",
        type=int,
        default=5432,
        required=False,
    )
    args = parse.parse_args()
    dbArgs = PostGressArgs(
        args.dbname, args.dbuser, args.dbpassword, args.dbhost, args.dbport
    )

    create_database(dbArgs)
