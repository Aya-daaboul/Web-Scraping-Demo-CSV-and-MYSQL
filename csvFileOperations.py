# Import the csv module to handle CSV files
import csv  

# Open a CSV file and store the file object in a variable
csvFile = open('test.csv', 'w', encoding='UTF8', newline='')  

writer = csv.writer(csvFile)  # Create a CSV writer object

# Write the header row containing column names
writer.writerow(['number', 'number plus 2', 'number times 2'])

# Loop to generate and write multiple rows of data
for i in range(10):
    writer.writerow([i, i + 2, i * 2])  # Write a row with number, number+2, and number*2

# Manually close the file after writing
csvFile.close()  