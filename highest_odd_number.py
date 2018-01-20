#!/usr/bin/Python
""" from Guutag book "Introduction to Computation and Programming using Python".
This is "Finger exercise #1 from page 16."""

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
