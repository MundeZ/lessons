import pandas as pd
import sqlite3
import numpy as np
import os
import sys


class SQLITE:
    
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __create_connection(self):
        self.connection = sqlite3.connect(self.db_name)
        
        
        
    def __close_connection(self):
        self.connection.close()

        
        
    def get_data_from_sql(query):

        self.__create_connection()
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        datafrombd =  res.fetchall()
        self.__connection.close()
        
        return datafrombd

    