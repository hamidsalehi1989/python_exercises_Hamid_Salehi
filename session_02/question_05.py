miles = int(input('Enter the distance(km) : '))
fixed_fare = 20000
new_miles= miles - 2
extra = new_miles*5000
if miles < 2:
    print('taxi fare : ',fixed_fare)
elif miles > 2 :
    new_fare = extra + fixed_fare 
    print('taxi fare : ',new_fare)
