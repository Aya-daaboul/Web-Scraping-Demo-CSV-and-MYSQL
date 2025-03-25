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

# Define the INSERT query
query = "INSERT INTO book (id, title, decription, cover) VALUES (%s, %s, %s, %s)"

# List of 10 books to insert
books = [
    (1, "The Great Gatsby", "A novel about wealth and love", "gatsby.jpg"),
    (2, "1984", "novel about a totalitarian regime", "1984.jpg"),
    (3, "To Kill a Mockingbird", "racism and justice", "mockingbird.jpg"),
    (4, "Pride and Prejudice", "manners and marriage", "pride.jpg"),
    (5, "Moby-Dick", "obsession and revenge", "mobydick.jpg"),
    (6, "War and Peace", "Napoleonic Wars", "warpeace.jpg"),
    (7, "Crime and Punishment", "guilt and redemption", "crime.jpg"),
    (8, "The Catcher in the Rye", "teenage rebellion", "catcher.jpg"),
    (9, "The Lord of the Rings", "good and evil", "lotr.jpg"),
    (10, "Harry Potter ", "magical journey", "hp1.jpg")
]

# Execute the queries
cursor.executemany(query, books)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("10 books inserted successfully!")