total = 0
l = []
while True:
    number = input("Enter your jumping height(m) : ")
    if number.isdigit() == max(l):
        print('new record added ! ','new hit by now is : ',max(l))
    elif number.isdigit() == min(l) :
        break
        print('new record added ! ','new hit by now is : ',min(l))
    else:
        l.append(number)
    total += number

print("The sum is:", total)








  

l = []
while True:
    i = input('Enter: ')
    if i.lower() == 'exit' :
        break
    else:
       l.append(i)
print(l)