# write to file in pyhton
# hello there
# subscribe to my channel

# w , a, r+

with open('file.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('please do it')