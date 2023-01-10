# Read and Write CSV files simultaneously in python

#firstname,lastname,age
#harshit,vashistha,500
#mohit,vashistha,500

# writer , Dictwriter
from csv import DictReader, DictWriter
with open('files.csv','r') as rf:
    with open('files2.csv','w',newlines='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writerheader()
        for row in csv_reader:
            fname, lname, age = row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
            })