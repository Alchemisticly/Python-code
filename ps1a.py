# Problem set 1A
#Ian Miner
#COllaborators: None
#Time Spent:



x = float(raw_input ('Enter credit card balance:'))
y = float(raw_input ('Enter annual interest rate:'))
z = float(raw_input ('Enter minimum monthly payment rate:'))
mmp = x*z               #minimal monthly payment
ip = float(y /(12*x))  # Interest paid (annual interest rate/12 months x Balance
pp = mmp- ip               #Principal paid
rb = x - pp              #remaining balance
for i in range (1,12+1):
    print ('Month: %s' %(i))
    print ('Minimum Monthly Payment:%.2f' %(mmp))
    print ('Principal Paid: % .2f' % (pp))
    print ('Remaining Balance: %.2f' %(rb))
print ('total paid: %.2f%(total))
print ('remaining balance: %.2f'%( ))
    
