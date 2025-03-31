# Import required libraries
from urllib.request import urlopen  # Used to open URLs and fetch data from web pages
from bs4 import BeautifulSoup  # Used for parsing and extracting data from HTML
import pymysql  # Used for connecting and interacting with a MySQL database


# Establish a connection to the MySQL database
conn = pymysql.connect(
    host='127.0.0.1',  # The database server's address (localhost in this case)
    user='root',  # Database username
    password='aya123',  # Database password 
    db='mysql',  # Name of the database 
    charset='utf8',  # Ensures that the database supports UTF-8 character encoding
    port=3306  # MySQL server port (default is 3306)
)

# Create a cursor object, which is used to execute SQL commands
cur = conn.cursor()

# Select the "scraping" database to work with (Make sure to create this database before running this code)
cur.execute("USE scraping")

# Function to store extracted data into the MySQL database
def store(title, content):
    """
    Stores the title and content of a Wikipedia page into the database.

    Parameters:
        title (str): The title of the Wikipedia article.
        content (str): The main content (paragraph) of the article.
    """
    # Execute an SQL INSERT command to add the data to the 'pages' table
    cur.execute('INSERT INTO pages (title, content) VALUES (%s, %s)', (title, content))
    
    # Commit the transaction to save changes in the database
    cur.connection.commit()

# Function to fetch links from a given Wikipedia article URL
def getContent(articleUrl):
    """
    Retrieves the title and other info based on what i specify.

    Parameters:
        articleUrl (str): The URL of the Wikipedia article (relative path).
    """
    # Open the Wikipedia page using the provided relative URL
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    
    # Parse the page content using BeautifulSoup
    bs = BeautifulSoup(html, 'html.parser')

    # Extract the title of the article (from the <h1> tag)
    title = bs.find('h1').get_text()

    # Extract the content
    # The content is inside a <div> with id="mw-content-text", and we get the first <p> tag inside it

    # content = bs.find('div', {'id': 'mw-content-text'}).find('p').get_text()

    content = ' '.join([div.get_text() for div in bs.find_all('div', {'class': 'hatnote navigation-not-searchable'})])

    #content = bs.find('div', {'class': 'shortdescription nomobile noexcerpt noprint searchaux'}).get_text()
    
    if content is None:
        print("No content found")
    

    # Store the extracted data into the database
    store(title, content)


def main():
    """
    Main execution function.
    """
    
    # Starting Wikipedia page (example: Python programming language)
    start_url = "/wiki/Python_(programming_language)"
    

    #start_url ="/wiki/Pizza" #404 error if pizza only

    print(f"Scraping: {start_url}")  # Log the scraping process
    getContent(start_url)  # Fetch and store data from Wikipedia

    # Close database connection
    cur.close()
    conn.close()

# Run the main function
if __name__ == "__main__":
    main()