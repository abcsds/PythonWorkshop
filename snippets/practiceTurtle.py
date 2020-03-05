from turtle import *


mode('logo')
clearscreen()
speed(0)

golden_angle = 137.5
golden_ratio = 1.618


def tree(size):
    if size >= 10:
        fd(size)
        lt(golden_angle / 2)
        tree(size / golden_ratio)
        rt(golden_angle)
        tree(size / golden_ratio)
        lt(golden_angle / 2)
        bk(size)


tree(200)
