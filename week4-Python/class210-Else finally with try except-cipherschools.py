# else and finally clause in exception handling

try:
    number = int(input('entre a number : '))
    
except ValueError:
    print("Please type integer !! s")    
except:
    print('unexpected error !!! ')
else:
    print(f'user input = {number}')
finally:
    print('finally block ........... ')