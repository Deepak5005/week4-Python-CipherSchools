# f = open('files.txt')
# f.read()
# f.close()

# with block
# context manager
with open('file1.txt') as f:
    data = f.read()
    print(data)
    
print(f.closed)