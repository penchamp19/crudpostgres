import sys
sys.path.insert(1, 'service')
import connectpostgres as con

# Functions Insert
def insert(fullname, email, age):
    try:
        conn = con.connectdb()
        cursor = conn.cursor()
        sql = "INSERT INTO person(fullname, email, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, (fullname, email, age))
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)

# Functions Select all person
def select_all():
    try:
        conn = con.connectdb()
        cursor = conn.cursor()
        sql = "select * from person"
        cursor.execute(sql)
        result = cursor.fetchall()
        rows = []
        tuple = ['รหัส','ชื่อ-สกุล','อีเมล','อายุ','วันที่สร้าง']
        rows.append(tuple)
        for data in result:
            rows.append(data)
        cursor.close()
        return rows
    except Exception as e:
        print(e)

# Functions select data by id from table person
def select_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "select * from person where id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    rows = [['รหัส','ชื่อ-สกุล','อีเมล','อายุ','วันที่สร้าง']]
    for data in result:
            rows.append(data)
    cursor.close()
    return rows

# Functions Update data by id
def update(id, fullname, email, age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "update person set fullname=%s, email=%s, age=%s where id=%s"
    cursor.execute(sql, (fullname, email, age, id))
    conn.commit()
    cursor.close()

# Functions delete data by id from table person
def delete(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "delete from person where id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
