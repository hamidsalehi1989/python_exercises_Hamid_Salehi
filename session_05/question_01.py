password = input('Enter password: ')

if  len(password) == 8 and any(not char.isalnum() for char in password):      
    print('password received')
else:
    raise ValueError('Password must contain at least 8 characters')
    raise ValueError('password must contain a special character')

            

