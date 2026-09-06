a = input('Enter a sentence: ')
words = a.lower().split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
        
most_rep_word = max(count, key=count.get)
print('The most repeated word: ',most_rep_word,' , ','Number of repetition: ',count[most_rep_word])
        
