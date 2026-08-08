b = list(input('Enter your jumping height(m) : '))
record_list = list(b)
new_hit = max(b[::])
for i in b:
    if i == min(b):
        print('This number has already been recorded, please enter new value : ')
    elif i == max(b):
        print('new record added ! ','new hit by now is : ',new_hit,'m')


# ask teacher !