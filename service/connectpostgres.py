import psycopg2
# create function for connect postgres db


def connectdb():
    # local

    try:
        # connection = psycopg2.connect(
        #     host='localhost',
        #     user='root',
        #     password='1234',
        #     db='postgres',
        #     charset='utf8mb4',
        #     port=3306,
        #     cursorclass=psycopg2.cursors.DictCursor)
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='sampledb',
            port=5432
        )
        return connection
    except Exception as e:
        print(e)


# test connection
# print(connectdb())
