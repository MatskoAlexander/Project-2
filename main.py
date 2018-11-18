from turtle import *

def rounds (x, y, r, n):
    while r > 0:
        up()
        goto(x, y - r)
        down()
        circle(r)
        up()
        rounds(x, y, r - n, n)
        break
    mainloop()
    hideturtle()
    done

def rectangle(x1, y1, x2, y2):
    up()
    goto(x1, y1)
    down()
    goto(x2, y1)
    goto(x2, y2)
    goto(x1, y2)
    goto(x1, y1)

def puzzle(x1, y1, a):
    x = [x1, x1, x1, x1]
    y = [y1, y1, y1, y1]
    b = [a, a, a, a]
    if b[1] > 5 and b[2] > 5 and  b[0] > 5 and b[3] > 5:
        rectangle(x[0] - b[0] / 2, y[0] - b[0] / 2, x[0] + b[0] / 2, y[0] + b[0] / 2)
        puzzle(x[0] - b[0] / 2, y[0] - b[0] / 2, b[0] / 2)
        puzzle(x[1] + b[1] / 2, y[1] + b[1] / 2, b[1] / 2)
        puzzle(x[2] + b[2] / 2, y[2] - b[2] / 2, b[2] / 2)
        puzzle(x[3] - b[3] / 2, y[3] + b[3] / 2, b[3] / 2)
    hideturtle()
    mainloop()

def strecoza(x, y, r):
    up()
    goto(x, y - r)
    down()
    circle(r)
    while r > 2:
        up()
        goto(x + r / 2, y - r / 2)
        down()
        circle(r / 2)
        up()
        goto(x - r / 2, y - r / 2)
        down()
        circle(r / 2)
        strecoza(x - r / 2, y, r / 2)
    strecoza(x - r / 2, y, r / 2)

    hideturtle()
    mainloop()

def triangle(x1, y1, x2, y2, x3, y3):
    while (x1 + x2) / 2 > 2:
        up()
        goto(x1, y1)
        down()
        goto(x2, y2)
        goto(x3, y3)
        goto(x1, y1)
        triangle((x1 + x2) / 2, (y1 + y2) / 2, (x2 + x3) / 2, (y2 + y3) / 2, (x1 + x3) / 2, (y1 + y3) / 2)
    hideturtle()
    mainloop



reset
speed(0)
answer = numinput('Что вы хотите нарисовать?', '1)Концентрические окружности\n2)Стрекоза\n3)Квадратики\n4)Треугольники', 0, minval=1, maxval=4)
if answer == 1:
    rounds(numinput('Координаты центра окружности', 'Введите xc', 0, minval=-300, maxval=300),
        numinput('Координаты центра окружности', 'Введите yc', 0, minval=-300, maxval=300),
        numinput('Окружность', 'Введите радиус r ', 0, minval=0, maxval=300),
        numinput('Расстояние между дугами окружностей', 'Введите расстояние между дугами окружностей', 0,
                minval=1, maxval=300))
elif answer == 2:
    strecoza(numinput('Центр стрекозы x', 'Введите x', 0, minval=-500, maxval=500),
              numinput('Центр стрекозы y', 'Введите y', 0, minval=-500, maxval=500),
              numinput('Радиус', 'Введите радиус', 0, minval=-500, maxval=500),)
elif answer == 3:
    puzzle(numinput('Координаты центра квадрата', 'Введите x', 0, minval=-500, maxval=500),
           numinput('Координаты центра квадрата', 'Введите y', 0, minval=-500, maxval=500),
           numinput('Ребро квадрата', 'Введите a', 0, minval=1, maxval=512))
elif answer == 4:
    triangle(numinput('Координаты 1 точки', 'Введите x1', 0, minval=-500, maxval=500),
             numinput('Координаты 1 точки', 'Введите y1', 0, minval=-500, maxval=500),
             numinput('Координаты 2 точки', 'Введите x2', 0, minval=-500, maxval=500),
             numinput('Координаты 2 точки', 'Введите y2', 0, minval=-500, maxval=500),
             numinput('Координаты 3 точки', 'Введите x3', 0, minval=-500, maxval=500),
             numinput('Координаты 3 точки', 'Введите y3', 0, minval=-500, maxval=500))