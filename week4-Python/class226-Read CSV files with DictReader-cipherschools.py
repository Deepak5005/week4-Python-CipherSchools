# Read CSV files with DictReader in Python

#name,email,phone
#harshit,harshitvashisth@gmail.com,+919416614988
#mohit,mohitvashistha@gmail.com,+919416614988


from csv import DictReader
# ordered dict
with open('files.csv', 'r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['email'])