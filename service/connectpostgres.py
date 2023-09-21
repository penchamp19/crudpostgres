import psycopg2
# create function for connect postgres db


def connectdb():
    # local

    # try:
    #     connection = psycopg2.connect(
    #         host='localhost',
    #         user='postgres',
    #         password='1234',
    #         database='sampledb',
    #         port=5432
    #     )
    #     return connection
    # except Exception as e:
    #     print(e)
    try:
        connection = psycopg2.connect(
            host='dpg-ck5snnldrqvc73dv2kh0-a',
            user='root',
            password='UogxOvefAybDosSjMTIhOzF67YF2dexX',
            database='sampledb_12qn',
            port=5432
        )
        return connection
    except Exception as e:
        print(e)


# test connection
# print(connectdb())
