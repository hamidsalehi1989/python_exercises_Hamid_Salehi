a = input('Enter a sentence: ')
words = a.lower().split()
count = {}
longest_word = []
max_length = 0

for word in words:
    if len(word)>max_length:
        longest_word = word
    elif len(word) == max_length:
        longest_word.append(word)
        
print('The longest word(s) : ',longest_word)
print('Maximum length: ',len(longest_word))


   

        