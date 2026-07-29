purchase_amount = float(input('Enter purchase amount (Toman) : '))
i = purchase_amount
if i > 1000000:
    print('Total amount :',0.85*i,'Toman')
elif 500000<= i <= 1000000:
    print('Total amount :',0.9*i,'Toman')
else:
    print('Total amount :',i,'Toman')
