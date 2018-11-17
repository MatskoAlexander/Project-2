from turtle import *

def rounds (x, y, r):
    while r > 0:
        up()
        goto(x, y - r)
        down()
        circle(r)
        up()
        rounds(x, y, r - 5)
        break
    mainloop()

reset
rounds(, , )
