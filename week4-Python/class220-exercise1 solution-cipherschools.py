# 15
# solution
# Harshit's salary is 100
# Mohit's salary is 50
with open('salary.txt','r') as rf:
    with open('output.txt', 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary} ')