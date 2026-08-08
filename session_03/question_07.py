c1 = input('Enter first color : ')
c2 = input('Enter second color : ')
c3 = input('Enter third color : ')
if c1==c2 or c2==c3 or c1==c3 :
    print('Two colors are similar')
elif c1==c2 and c2==c3 :
    print('Three colors are similar')
else:
    print('colors are different')
