# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

title_input = input('What movie would you like to search? ')
found = False

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # \t if delimited by tab
    #print(csvreader)
    # csv_header = next(csvreader)

    for row in csvreader:
        if row[0].lower().replace(' ','') == title_input.lower().replace(' ',''):
            print(f'{row[0]} is rated {row[1]} with a rating of {row[5]}')

            found = True

            break

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader
        

    # while row[0] != title_input:
    # print(row)
