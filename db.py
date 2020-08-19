import sqlite3
from sqlite3 import Error
class mysqlite:
    def __init__(self,db_file):
        self.conn=self._create_connection(db_file)
        
    
    def _create_connection(self,db_file)->sqlite3.Connection:
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error:
            print(Error)
        return None
        
    def qurey(self,qry):
        self.conn.execute(qry)
        self.conn.commit()
    def rows(self,qry):
        cur = self.conn.cursor()
        cur.execute(qry)
        rows = cur.fetchall()
        return rows


