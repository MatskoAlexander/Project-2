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
rounds(numinput("Координаты центра окружности", "Введите xc", 0, minval=-300, maxval=300),
       numinput("Координаты центра окружности", "Введите yc", 0, minval=-300, maxval=300),
       numinput("Окружность", "Введите радиус r ", 0, minval=0, maxval=300))
