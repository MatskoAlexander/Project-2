from turtle import *

def rounds (x, y, r, n):
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

def puzzle(x1, y1, a, k):
    if a > k:
        rectangle(x1 - a / 2, y1 - a / 2, x1 + a / 2, y1 + a / 2)
        rectangle(x1 - a / 2 - a / 4, y1 - a / 2 - a / 4, x1 - a / 4, y1 - a / 4)
        rectangle(x1 - a / 2 - a / 4, y1 + a / 2 + a / 4, x1 - a / 4, y1 + a / 4)
        rectangle(x1 + a / 2 + a / 4, y1 + a / 2 + a / 4, x1 + a / 4, y1 + a / 4)
        rectangle(x1 + a / 2 + a / 4, y1 - a / 2 - a / 4, x1 + a / 4, y1 - a / 4)
        puzzle(x1 - a / 2, y1 - a / 2, a / 2, k)
        puzzle(x1 - a / 2, y1 + a / 2, a / 2, k)
        puzzle(x1 + a / 2, y1 + a / 2, a / 2, k)
        puzzle(x1 + a / 2, y1 - a / 2, a / 2, k)


def strecoza(x, y, r, k):
    if r > k:
        up()
        goto(x, y - r)
        down()
        circle(r)
        up()
        goto(x + r / 2, y - r / 2)
        down()
        circle(r / 2)
        up()
        goto(x - r / 2, y - r / 2)
        down()
        circle(r / 2)
        strecoza(x - r / 2, y, r / 2, k)
        strecoza(x + r / 2, y, r / 2, k)


def triangle(x1, y1, x2, y2, x3, y3):
    if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2) > 4:
        up()
        goto(x1, y1)
        down()
        goto(x2, y2)
        goto(x3, y3)
        goto(x1, y1)
        goto((x1 + x2) / 2, (y1 + y2) / 2)
        goto((x2 + x3) / 2, (y2 + y3) / 2)
        goto((x1 + x3) / 2, (y1 + y3) / 2)
        goto((x1 + x2) / 2, (y1 + y2) / 2)
        triangle((x1 + (x1 + x2) / 2) / 2, (y1 +(y1 + y2) / 2) / 2, (x1 + (x1 + x3) / 2) / 2, (y1 + (y1 + y3) / 2) / 2,
                 ((x1 + x2) / 2 + (x1 + x3) / 2) / 2, ((y1 + y2) / 2 + (y1 + y3) / 2) / 2)
        triangle(((x1 + x2) / 2 + x2) / 2, (y2 + (y1 + y2) / 2) / 2, (x2 + (x2 + x3) / 2) / 2,
                 (y2 + (y2 + y3) / 2) / 2, ((x1 + x2) / 2 + (x2 + x3) / 2) / 2, ((y1 + y2) / 2 + (y2 + y3) / 2) / 2)
        triangle((x3 + (x1 + x3) / 2) / 2, (y3 + (y1 + y3) / 2) / 2, (x3 + (x2 + x3) / 2) / 2, (y3 + (y2 + y3) / 2) / 2,
                 ((x3 + x2) / 2 + (x1 + x3) / 2) / 2, ((y3 + y2) / 2 + (y1 + y3) / 2) / 2)
        triangle(((x3 + x2) / 2 + (x1 + x3) / 2) / 2, ((y3 + y2) / 2 + (y1 + y3) / 2) / 2,
                ((x1 + x2) / 2 + (x2 + x3) / 2) / 2, ((y1 + y2) / 2 + (y2 + y3) / 2) / 2,
                ((x1 + x2) / 2 + (x1 + x3) / 2) / 2, ((y1 + y2) / 2 + (y1 + y3) / 2) / 2)





reset
speed(0)
hideturtle()
answer = numinput('Что вы хотите нарисовать?', '1)Концентрические окружности\n2)Стрекоза\n3)\'Пазл\'\n4)Треугольники',
                  0, minval=1, maxval=4)
if answer == 1:
    rounds(numinput('Координаты центра окружности', 'Введите xc', 0, minval=-300, maxval=300), numinput
    ('Координаты центра окружности', 'Введите yc', 0, minval=-300, maxval=300), numinput('Окружность',
    'Введите радиус r ', 0, minval=0, maxval=300),numinput('Расстояние между дугами окружностей',
    'Введите расстояние между дугами окружностей', 0, minval=1, maxval=300))

elif answer == 2:
    strecoza(numinput('Центр стрекозы x', 'Введите x', 0, minval=-500, maxval=500), numinput
    ('Центр стрекозы y', 'Введите y', 0, minval=-500, maxval=500), numinput('Радиус', 'Введите радиус', 0,
    minval=-500, maxval=500), numinput('Ограничение по размеру', 'Введите ограничение по размеру глаз', 0, minval=1,
    maxval=500))

elif answer == 3:
    puzzle(numinput('Координаты центра квадрата', 'Введите x', 0, minval=-500, maxval=500), numinput
    ('Координаты центра квадрата', 'Введите y', 0, minval=-500, maxval=500), numinput('Ребро квадрата', 'Введите a', 0,
    minval=1, maxval=700), numinput('Минимальное ребро квадрата', 'Введите k', 0, minval=1, maxval=700))

elif answer == 4:
    triangle(numinput('Координаты 1 точки', 'Введите x1', 0, minval=-500, maxval=500), numinput('Координаты 1 точки',
            'Введите y1', 0, minval=-500, maxval=500), numinput('Координаты 2 точки', 'Введите x2', 0, minval=-500, maxval=500),
            numinput('Координаты 2 точки', 'Введите y2', 0, minval=-500, maxval=500), numinput('Координаты 3 точки',
            'Введите x3', 0, minval=-500, maxval=500), numinput('Координаты 3 точки', 'Введите y3', 0, minval=-500, maxval=500))

mainloop()
