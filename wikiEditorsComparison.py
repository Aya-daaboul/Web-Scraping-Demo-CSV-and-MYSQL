# Import necessary libraries
import csv  
from urllib.request import urlopen  
from bs4 import BeautifulSoup  

# Open the Wikipedia page containing the table
html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')  

# Parse the HTML content using BeautifulSoup
bs = BeautifulSoup(html, 'html.parser')  

# Find the first table with class 'wikitable' (main comparison table)
table = bs.findAll('table', {'class': 'wikitable'})[0]  

# Extract all rows from the table
rows = table.findAll('tr')  

# Open a CSV file to write data
csvFile = open('editors.csv', 'w', encoding='UTF8', newline='')  

# Create a CSV writer object
writer = csv.writer(csvFile)  

# Iterate through table rows and extract data
for row in rows:
    csvRow = []  # Create an empty list for row data
    for cell in row.findAll(['td', 'th']):  # Extract all table data and headers
        csvRow.append(cell.get_text().strip())  # Get the text, remove extra spaces
    writer.writerow(csvRow)  # Write the row to the CSV file

# Close the CSV file
csvFile.close()  

print("CSV file 'editors.csv' has been created successfully.")