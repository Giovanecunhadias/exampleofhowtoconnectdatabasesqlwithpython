from db_connector import DBConnection

# Create an instance of the DBConnection class
db_connection = DBConnection()

# Connect to the database
connection = db_connection.connect()

# Example database operation
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()

# Display result
print('Result:')
for row in result:
    print(row)

# Close the connection
db_connection.close_connection()
