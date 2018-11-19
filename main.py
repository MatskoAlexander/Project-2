from turtle import *
import local


def rounds(x, y, r, n):
    if r > 0:
        up()
        goto(x, y - r)
        down()
        circle(r)
        up()
        rounds(x, y, r - n, n)


def rectangle(x1, y1, x2, y2):
    up()
    goto(x1, y1)
    down()
    goto(x2, y1)
    goto(x2, y2)
    goto(x1, y2)
    goto(x1, y1)


def puzzle(x, y, a, k):
    if a >= k:
        rectangle(x - a / 2, y - a / 2, x + a / 2, y + a / 2)
        puzzle(x - a / 2, y - a / 2, a / 2, k)
        puzzle(x - a / 2, y + a / 2, a / 2, k)
        puzzle(x + a / 2, y + a / 2, a / 2, k)
        puzzle(x + a / 2, y - a / 2, a / 2, k)


def strecoza(x, y, r, k):
    if r >= k:
        up()
        goto(x, y - r)
        down()
        circle(r)
        strecoza(x - r / 2, y, r / 2, k)
        strecoza(x + r / 2, y, r / 2, k)


def triangle(x1, y1, x2, y2, x3, y3, k):
    if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2) >= k and ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2) >= k and \
            ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2) >= k:
        up()
        goto(x1, y1)
        down()
        goto(x2, y2)
        goto(x3, y3)
        goto(x1, y1)
        triangle(x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2, k)
        triangle(x2, y2, (x1 + x2) / 2, (y1 + y2) / 2, (x2 + x3) / 2, (y2 + y3) / 2, k)
        triangle(x3, y3, (x3 + x2) / 2, (y3 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2, k)


reset()
speed(0)
hideturtle()
answer = numinput(local.choose1, local.choose2, 0, minval=1, maxval=4)
if answer == 1:
    title(local.rounds0)
    rounds(numinput(local.rounds11, local.rounds12, 0, minval=-500, maxval=500),
           numinput(local.rounds11, local.rounds22, 0, minval=-500, maxval=500),
           numinput(local.rounds31, local.rounds32, 0, minval=0, maxval=500),
           numinput(local.rounds41, local.rounds42, 0, minval=1, maxval=500))
elif answer == 2:
    title(local.strecoza0)
    strecoza(numinput(local.strecoza11, local.strecoza12, 0, minval=-500, maxval=500),
             numinput(local.strecoza11, local.strecoza22, 0, minval=-500, maxval=500),
             numinput(local.strecoza31, local.strecoza32, 0, minval=-500, maxval=500),
             numinput(local.strecoza41, local.strecoza42, 0, minval=1, maxval=500))
elif answer == 3:
    title(local.puzzle0)
    puzzle(numinput(local.puzzle11, local.puzzle12, 0, minval=-500, maxval=500),
           numinput(local.puzzle11, local.puzzle22, 0, minval=-500, maxval=500),
           numinput(local.puzzle31, local.puzzle32, 0, minval=1, maxval=500),
           numinput(local.puzzle41, local.puzzle42, 0, minval=1, maxval=500))
elif answer == 4:
    title(local.triangle0)
    triangle(numinput(local.triangle11, local.triangle12, 0, minval=-500, maxval=500),
             numinput(local.triangle11, local.triangle22, 0, minval=-500, maxval=500),
             numinput(local.triangle31, local.triangle32, 0, minval=-500, maxval=500),
             numinput(local.triangle31, local.triangle42, 0, minval=-500, maxval=500),
             numinput(local.triangle51, local.triangle52, 0, minval=-500, maxval=500),
             numinput(local.triangle51, local.triangle62, 0, minval=-500, maxval=500),
             numinput(local.triangle71, local.triangle72, 0, minval=1, maxval=500))
mainloop()
