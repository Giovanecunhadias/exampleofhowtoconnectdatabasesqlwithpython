# exampleofhowtoconnectdatabasesqlwithpython

Requirements:

pip install mysql-connector-python

import mysql.connector

class DBConnection:
    def __init__(self, host='name of your host', user='your_user', password='your_password', database='name_of_your_database'):
        self.host =  host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()

