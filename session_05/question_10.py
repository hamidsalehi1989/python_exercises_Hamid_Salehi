sen_1 = input('Enter first sentence: ')
sen_2 = input('Enter second sentence: ')
list_sen1 = sen_1.lower().split()
list_sen2 = sen_2.lower().split()
list_similar_word = [] 
count = {}
for i in list_sen1:
    for j in list_sen2:
        if j in i:
            list_similar_word.append(j)
            if j in count:
                count[j]
            else:
                count[j]=1

print('Common words : ')
print(list_similar_word)

