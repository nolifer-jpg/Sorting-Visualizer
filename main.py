import time
import turtle

import numpy as np

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(15)
arr = np.random.randint(10, 200, size=20)


def draw_bar(data_array):
    t.up()
    t.goto(-300, -200)
    for number in arr:
        t.down()
        t.seth(90)
        t.forward(number)
        t.backward(number)
        t.up()
        t.seth(0)
        t.forward(20)


def bubble_sort(data_array):
    for i in range(len(data_array)):
        for j in range(len(data_array) - i - 1):
            if data_array[j] > data_array[j + 1]:
                data_array[j], data_array[j + 1] = data_array[j + 1], data_array[j]
                draw_bar(data_array)
                time.sleep(0.1)


bubble_sort(arr)
turtle.done()
