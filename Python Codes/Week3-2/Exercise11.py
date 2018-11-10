import csv
import os

csvpath = os.path.join('..', 'Resources', 'web_starter.csv')
title, price = []
subscriber_count = []
num_reviews = []
course_length = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscriber_count.append(row[5])
        num_reviews.append(row[6])
        course_length.append(row[9])

    new_list = zip(title,price,subscriber_count,num_reviews,course_length)
    #print(list(new_list))

    output_file = os.path.join("udemy_output.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["title", "price", "subscriber count","number of reviews","course length"])

    writer.writerows(new_list)

    #for row in new_list:
        #writer.writerow(row)