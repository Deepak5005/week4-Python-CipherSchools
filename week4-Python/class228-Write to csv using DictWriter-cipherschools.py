# Write to csv using DictWriter in Python
from csv import DictWriter
with open('final.csv','w',newlines='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    csv_writer.writerows([
        {'firstname':'harshit','lastname':'vashistha','age':500},
        {'firstname':'harshit','lastname':'vashistha','age':500},
        {'firstname':'harshit','lastname':'vashistha','age':500}
    ])