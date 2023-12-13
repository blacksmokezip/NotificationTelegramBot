import psycopg2
from psycopg2 import sql


query = sql.SQL(
                "SELECT * FROM {} WHERE {}=%s"
            )


def get_connection(database):
    connection = psycopg2.connect(database)
    return connection


def add_user(connection, id, nickname):
    with connection.cursor() as cur:
        cur.execute(
            sql.SQL(
                "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)"
            ).format(
                sql.Identifier("users"),
                sql.Identifier("user_id"),
                sql.Identifier("nickname"),
                sql.Identifier("timezone")
            ), [id, nickname, 'Europe/Moscow']
        )
        connection.commit()


def update_timezone(connection, id, timezone):
    with connection.cursor() as cur:
        cur.execute(
            sql.SQL(
                "UPDATE {} SET {} = %s WHERE {}=%s"
            ).format(
                sql.Identifier("users"),
                sql.Identifier("timezone"),
                sql.Identifier("user_id")
            ), [timezone, id]
        )
        connection.commit()


def add_a_notification(connection, *args):
    with connection.cursor() as cur:
        cur.execute(
            sql.SQL(
                "INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s, %s, %s)"
            ).format(
                sql.Identifier("notifications"),
                sql.Identifier("user_id"),
                sql.Identifier("hash"),
                sql.Identifier("name"),
                sql.Identifier("date")
            ), [args[0], args[1], args[2], args[3]]
        )
        connection.commit()


def delete_notification(connection, hash_):
    with connection.cursor() as cur:
        cur.execute(
            sql.SQL(
                "DELETE FROM {} WHERE {}=%s"
            ).format(
                sql.Identifier("notifications"),
                sql.Identifier("hash")
            ), [hash_]
        )
        connection.commit()


def select(connection, table, column, data):
    with connection.cursor() as cur:
        cur.execute(
            query.format(
                sql.Identifier(table),
                sql.Identifier(column)
            ), [data]
        )
        result = cur.fetchall()
        return result
