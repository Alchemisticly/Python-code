#!/usr/bin/Python
# Problem set 1B
#Ian Miner
#Collaborators: None
#Time Spent:



x = float(raw_input ('Enter credit card balance:'))
y = float(raw_input ('Enter annual interest rate:'))

mir = y / 12     # montly interest rate
mp = 10           # monthly payment
mb = (x + x * mir) - mp     # monthly balance
month = 0


while mp < x/12:
    for i in range(1,13):
        month = 0
        mb = x + x * mir - mp
        mp += 10
        month += month
        balance = mb
print ('RESULT')
print 'Monthly payment to pay', x,
print ' in one year is', mp, ' per month'
print (' Number of months needed:% ' %(month))
print ('Balance: %' %(balance))
