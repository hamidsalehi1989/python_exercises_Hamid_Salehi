text = input('Enter string : ')
word = text.lower().strip()
count={}
for letter in word:
    if letter in count:
        count[letter]+=1
    elif letter == '' :
        continue
    else:
        count[letter]=1
        
print(count)
