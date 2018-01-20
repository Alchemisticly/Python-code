#!/usr/bin/Python
""" from Guttag book "Introduction to Computation and Programming using Python".
This is "Finger exercise #2 from page 20. This program asks for ten numbers
but will take more or less,and return the highest odd number
"""

nums = raw_input('Please enter 10 numbeers sepeated by a comma: ')
nums = eval(nums) # eval allows list to be seperated and processed.
odd_nums = [] # new list of only odd numbers from the raw_input.

for i in nums:
    if i % 2 == 1: # for loop to find the odd numbers from the nums list.
        odd_nums.append(i)
        odd_nums.sort() # sorts odd_nums list from small to largest.
print odd_nums.pop() # pop takes the last (highest) number from the list.
