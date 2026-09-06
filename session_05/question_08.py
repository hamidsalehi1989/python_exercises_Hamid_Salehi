a = input('Enter a string : ') 
special_char = ['!','@','#','$','%','&','*','_']
words = a.lower().strip().split()
char_count = a.lower().strip().split()
char_count = {}
word_count = {}
c = 0
#d = len(word_count)
e = 0
w = 0
u = 0
r = 0
for i in a:
    if i.isdigit() :
        c+=1
            
    elif i.isupper():
        e+=1
                        
    elif i.islower():
        w+=1
                          
    elif i.isspace():
        u+=1
                      
    elif i in special_char:
        r+=1

for char in a.lower(): 
    if char in char_count:
        char_count[char] += 1 
    else: char_count[char] = 1
        
for word in words:
    if word in word_count: 
       word_count[word] += 1 
    else: word_count[word] = 1

most_rep_word = max(word_count, key=word_count.get)
most_rep_char = max(char_count, key=char_count.get)
longest_word = max(words, key=len)
shortest_word = min(words,key=len)

print('No of digits: ',c)
print('No of words: ',len(words))
print('No of upper words: ',e) 
print('No of lower words: ',w) 
print('No of spaces: ',u) 
print('No of special characters: ',r)
print('The most repeated word: ',most_rep_char)
print('The most repeated character: ',most_rep_char) 
print('longest word: ',longest_word)
print('shortest word: ',shortest_word)


