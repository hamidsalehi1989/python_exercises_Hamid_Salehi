a = int(input('Enter a number:'))
input_list =[]
for i in range(a):
    value = input(f"Enter value {i+1}: ")
    input_list.append(value)
if i == 0:
    print('sum : ',sum(input_list))
else:
    print(i+1)

#ask !!!
