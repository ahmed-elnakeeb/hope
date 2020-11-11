import sqlite3
from sqlite3 import Error
class mysqlite:
    def __init__(self,db_file):
        """initialize connection with db file or create new"""
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
        """executes given query """
        try:
            self.conn.execute(qry)
            self.conn.commit()
        except Error as e:
            print(e)
    def rows(self,qry)->list:
        """ return the selected rows"""
        try:
            cur = self.conn.cursor()
            cur.execute(qry)
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)


