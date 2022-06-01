import psycopg2


def getConnection():
    connection = psycopg2.connect(
    database="project_0",
    user="project_0",
    password="Revature1",
    host="project-0.cppriojucxmm.us-east-1.rds.amazonaws.com",
    port="5432"
    )
    return connection


def executeSimpleQuery(sql,*args):
    connection=getConnection()
    result=executeQuery(connection,sql,*args)
    connection.commit()
    close(connection)
    return result

def executeQuery(connection,sql,*args):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (args))
        result = cursor.fetchall()
        return result
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()


def commit(connection):
    connection.commit()


def close(connection):
    if connection is not None:
        connection.close()