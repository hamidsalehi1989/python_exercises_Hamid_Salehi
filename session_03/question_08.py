withdrawl_amount = int(input('Enter cash withdrawl amount : '))
account_balance = int(input('Enter your account balance : '))
# minimum amount for card balance to recieve cash is set 250,000 toman
if withdrawl_amount>0 and account_balance>withdrawl_amount+250000:
    print('transaction is successful')
elif withdrawl_amount>0 and account_balance<=withdrawl_amount+250000:
    print('Your card balance is not sufficient')
elif withdrawl_amount<=0:
    print('Error')
