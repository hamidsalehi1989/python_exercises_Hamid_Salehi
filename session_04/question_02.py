a = print('Select one of the following words --> Rock/Paper/Scissors')
b = input('Enter your favourite word : ')
list_words = ['rock','paper','scissors']
import random
random_word = random.choice(list_words)
if b == random_word:
    print('Select a word again !')
elif b != random_word:
    print('Again choose a word !')
    print('Correct answer is :',random_word)
elif b == 'exit' or b == 'Exit' :
    print('Game is over')

