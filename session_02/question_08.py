clock = int(input('Enter time : '))
if 0 <= clock <= 12:
    print('Good morning!')
elif 12 < clock <= 15:
    print('Good afternoon!')
elif 15 < clock <= 18:
    print('Good evening!')
elif 18 < clock <= 23:
    print('Good night!')
else:
    print('Error')
    
