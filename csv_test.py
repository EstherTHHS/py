# add module for better read and write 
import csv

# with open('csvTest.csv') as file:
#     csv_file=csv.reader(file)
#     # open(csv_file)
#     for line in csv_file:
#         print(line)

# must be list type when read and write csv

# write csv data

data=[
    ['Joe','student',21],
    ['Mary','housewife',32],
    ['Mike','lawyer',32]
    
    ]

with open('csvWriteTest.csv','w',newline='') as file:
    csvtest=csv.writer(file)
    csvtest.writerows(data)
