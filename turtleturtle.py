import random
from tkinter import *
from turtle import *
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
turtle.speed(0)

colors = ['#5E366A','#0CCA98']

num = int(input("What number would you like?"))

for i in range(int(num)*500000000000000000000):
    turtle.forward(5*i)

    #Replace with number in photo.
    turtle.right((num)/0.000000000000000000000000000000000000000000000000000000000123456789)
	
    if i%2 == 0:
        turtle.color(colors[0])
    else:
        turtle.color(colors[1])







