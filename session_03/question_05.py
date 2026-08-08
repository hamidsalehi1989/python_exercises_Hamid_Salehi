a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = input('Choose add for + , sub for - , mul for * and div for / :')
d = ['add','sub','mul','div']
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
if c=='add':
    print('Output number is ',add(a,b))
elif c=='sub' :
    print('Output number is ',sub(a,b))
elif c=='mul':
    print('Output number is ',mul(a,b))
elif c=='div':
    print('Output number is ',div(a,b))
else:
    print('Enter both values again!')
    