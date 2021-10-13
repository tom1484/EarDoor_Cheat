import pymysql
import json


class Database:

    def __init__(self, host, database, user, password, table):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.table = table

    def connect(self):
        while True:
            try:
                self.conn = pymysql.connect(host=self.host, database=self.database,
                                            user=self.user, password=self.password)
                return

            except:
                pass

    def select_records(self, name):
        sql = f'SELECT records FROM {self.table} WHERE name=\'{name}\';'

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)

            raw = cursor.fetchone()[0]
            return json.loads(raw)
        except:
            return None

    def select_image(self, name):
        sql = f'SELECT image FROM {self.table} WHERE name=\'{name}\';'
        # print(sql)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)

            return cursor.fetchone()[0]
        except:
            return None

    def update_records(self, name, records):
        sql = f'UPDATE {self.table} SET records=\'{records}\' WHERE name=\'{name}\';'
        # print(sql)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

            return 1
        except:
            return None

    def update_image(self, name, image):
        sql = f'UPDATE {self.table} SET image=\'{image}\' WHERE name=\'{name}\';'
        # print(sql)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

            return 1
        except:
            return None

    def insert(self, name):
        sql = f'INSERT INTO {self.table} (name, records) VALUES (\'{name}\', \'[]\');'
        # print(sql)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

            return 1
        except:
            return None

    def delete(self, name):
        sql = f'DELETE FROM {self.table} WHERE name=\'{name}\';'
        # print(sql)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

            return 1
        except:
            return None

    def add_record(self, name, record):
        records = self.select_records(name)

        records.append(record)
        records = json.dumps(records)
        self.update_records(name, records)
