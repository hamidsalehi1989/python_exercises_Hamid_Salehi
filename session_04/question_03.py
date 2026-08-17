a = input('Enter your password : ')
if len(a) == 8 and a[0:4].isalpha() and a[5:8].isdigit():
    print('Valid')
else:
    print('Invalid')
    

    