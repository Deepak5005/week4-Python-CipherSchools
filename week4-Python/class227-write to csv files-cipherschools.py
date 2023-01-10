# write to CSV File in python

# writer , DictWriter
from csv import writer
with open('file3.csv','w',newline='') as f:
    csv_writer = writer(f)
    # method - writerow, writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['mohit','INDIA'])
    # csv_writer.writerow(['harshit','INDIA'])
    
    
    csv_writer.writerow([['name','contry'],['mohit','INDIA'],['harshit','INDIA']])