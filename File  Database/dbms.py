import mysql.connector


class DBhelper:
    def __init__(self):
        try:
            self.conn= mysql.connector.connect(host="localhost",username="root",
                    password="",databse="sample")
            self.cur=self.conn.cursor()
        except:
            print("Connected to database")
        else:
            print("Connection failed")