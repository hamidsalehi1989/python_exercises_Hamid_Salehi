a = float(input('enter a number : '))
import secrets
b = secrets.randbits(10)
if a > b:
    print('The correct number is:',b)
    print('Enter another number and insert smaller amount this time!')
elif a < b:
    print('The correct number is:',b)
    print('Enter another number and insert greater amount this time!')
elif a == b:
    print('Congrats ! your guess was correct.')
    



