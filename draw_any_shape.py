#!/usr/bin/python

""" program to make any shape with even straight lines ( triangle,
square,pentagon...etc)"""

import turtle # callsthe drawing program turtle.

def draw_any_shape(int,length): # function name, int=number of sides of shape.
	for _ in range(int): # forloop
		turtle.forward(length) # move line forward as per (length)
		turtle.right(360/int) # turns to angle as per shape.


if __name__=='__main__':
	draw_any_shape(5,5)
	while(True):
		pass
