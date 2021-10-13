import pymysql

class CNN:
    def __init__(self):
        pass

    def detect(self):
        conn = pymysql.connect(host='localhost', database='cheat', user='cheat', password='')
        sql = f'SELECT status FROM cheat WHERE 1;'
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchone()[0], 0
