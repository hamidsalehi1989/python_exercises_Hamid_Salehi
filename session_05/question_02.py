a = input('Enter string: ')
repeated_char = set()
for i in a:
    if i not in repeated_char:
        print(i,end='')
        repeated_char.add(i)
        
        
            

     