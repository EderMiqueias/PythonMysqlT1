import mysql.connector


def getdb():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="yourpwd",
        database="testePythonMysql"
    )
