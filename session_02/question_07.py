card_num = input('Enter your card number : ')
if card_num[0:4] == '6219' and len(card_num) ==16 :
    print('This card has been issued by Bank Mellat')
else:
    print('Your card number is not valid or has been issued by another bank')

   