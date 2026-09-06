a = input('Enter a string : ')
special_char = ['!','@','#','$','%','&','*','_']
c = 0
d = 0
e = 0
w = 0
u = 0
r = 0
for i in a:
    if i.isdigit() :
        c+=1
            
    elif i.isupper():
        e+=1
        d+=1
                
    elif i.islower():
        w+=1
        d+=1
                  
    elif i.isspace():
        u+=1
                      
    elif i in special_char:
        r+=1
    
print('No of digits: ',c)
print('No of words: ',d)
print('No of upper words: ',e) 
print('No of lower words: ',w) 
print('No of spaces: ',u) 
print('No of special chars: ',r)


