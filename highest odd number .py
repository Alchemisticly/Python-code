x= int (raw_input ('Enter intenger: '))
y = int (raw_input ( 'Enter intenger: '))
z = int (raw_input ('Enter intenger: '))   
if x > y and x > z and x%2==1 :
    print x
elif y > z and y%2==1:
    print y
elif z > y and z %2==1:
    print z
else:
    print 'no odd numbers'
