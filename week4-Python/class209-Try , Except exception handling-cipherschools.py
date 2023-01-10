# Exception handling
# try except else finally

while True:
    try:
        age = int(input('entre your age')) # seven # 7
        break
    except ValueError:
        print('maybe you entered  string instead of number , try again')
    except:
        print('unexpected error ....')
        
if age < 18:
    print('You can\'t play this  game.')
else:
    print('you can play this game.')