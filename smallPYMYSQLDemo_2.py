import pymysql

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",       
    password="aya123",  
    database="test"    
)

# Create a cursor object
cursor = connection.cursor()

# Execute a simple query
cursor.execute("SELECT * FROM book") 

# Fetch and print the result
result = cursor.fetchall()
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()