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

def puzzle(x1, y1, a, k):
    x = [x1, x1, x1, x1]
    y = [y1, y1, y1, y1]
    b = [a, a, a, a]
    if b[1] > k and b[2] > k and  b[0] > k and b[3] > k:
        rectangle(x1 - a / 2, y1 - a / 2, x1 + a / 2, y1 + a / 2)
        rectangle(x1 - a / 2 - a / 4, y1 - a / 2 - a / 4, x1 - a / 4, y1 - a / 4)
        rectangle(x1 - a / 2 - a / 4, y1 + a / 2 + a / 4, x1 - a / 4, y1 + a / 4)
        rectangle(x1 + a / 2 + a / 4, y1 + a / 2 + a / 4, x1 + a / 4, y1 + a / 4)
        rectangle(x1 + a / 2 + a / 4, y1 - a / 2 - a / 4, x1 + a / 4, y1 - a / 4)
        puzzle(x[0] - b[0] / 2, y[0] - b[0] / 2, b[0] / 2, k)
        puzzle(x[0] - b[0] / 2, y[0] + b[0] / 2, b[0] / 2, k)
        puzzle(x[0] + b[0] / 2, y[0] + b[0] / 2, b[0] / 2, k)
        puzzle(x[0] + b[0] / 2, y[0] - b[0] / 2, b[0] / 2, k)

    hideturtle()


def strecoza(x1, y1, r1):
    r = [r1, r1, r1, r1]
    x = [x1, x1, x1, x1]
    y = [y1, y1, y1 , y1]
    up()
    goto(x1, y1 - r1)
    down()
    circle(r1)
    while r[0] > 4 and r[1] > 4 and r[2] > 4 and r[3] > 4:
        up()
        goto(x1 + r1 / 2, y1 - r1 / 2)
        down()
        circle(r1 / 2)
        up()
        goto(x1 - r1 / 2, y1 - r1 / 2)
        down()
        circle(r1 / 2)

        strecoza(x[0] - r[0] / 2, y[0], r[0] / 2)


    hideturtle()


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
           numinput('Ребро квадрата', 'Введите a', 0, minval=1, maxval=700),
           numinput('Минимальное ребро квадрата', 'Вдите k', 0, minval=1, maxval=700))
elif answer == 4:
    triangle(numinput('Координаты 1 точки', 'Введите x1', 0, minval=-500, maxval=500),
             numinput('Координаты 1 точки', 'Введите y1', 0, minval=-500, maxval=500),
             numinput('Координаты 2 точки', 'Введите x2', 0, minval=-500, maxval=500),
             numinput('Координаты 2 точки', 'Введите y2', 0, minval=-500, maxval=500),
             numinput('Координаты 3 точки', 'Введите x3', 0, minval=-500, maxval=500),
             numinput('Координаты 3 точки', 'Введите y3', 0, minval=-500, maxval=500))
mainloop()