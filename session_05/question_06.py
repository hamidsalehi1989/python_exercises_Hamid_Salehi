list_words = ['fraud','hack','scam','password','attack']
word = input('Enter a sentence : ')
words = word.lower().split() 
list_similar_word = [] 
count = {}
for i in words:
    for j in list_words:
        if j in i:
            list_similar_word.append(j)
            if j in count:
                count[j]
            else:
                count[j]=1

print('kalame moshabeh : ',list_similar_word)
print('tedade tekrar : ',count)







        
        