list_user = 'ali1405'
list_pass = 'ghGHj_8800_word'
attempts = 0
while attempts < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    user = username.lower()
    if user == list_user and password == list_pass :
        print('Login Successful')
        break
    else:
       attempts+=1 
       if attempts < 3:
           print('Attempts remaining :',3-attempts)
       else:
           print('Wrong username or password')
           
        
    
                    