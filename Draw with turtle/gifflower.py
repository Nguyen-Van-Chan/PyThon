#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle
 

turtle.setup(1200, 600)  

 



 

 

turtle.color("black", "red")

turtle.pensize(2)

turtle.speed(10)

turtle.up()  

turtle.goto(0, 50)

 

turtle.down()

 

 

def draw_heart(r, angle=45):

    """

    :param r: 

    :param angle: 

    :return: 

    """

    turtle.begin_fill()  

    turtle.seth(0)

    turtle.seth(angle)  

    turtle.circle(-r, 180)  

    turtle.fd(2 * r)  

    turtle.begin_poly()  

    x, y = turtle.get_poly()[0]  

    turtle.right(90)  

    turtle.fd(2 * r)  

    turtle.circle(-r, 180)

    turtle.end_fill()  

    return x, y

 

 

x_y = []

start_x = 0

for _ in range(4):

    turtle.goto(start_x, 50)

    turtle.down()  

    x_y.append(draw_heart(8))

    start_x += 50

    turtle.up()  

 

 



def draw_flower(x, y):

    """

    

    :param x: 

    :param y: 

    :return:

    """

    turtle.up()

    turtle.goto(x, y)

    turtle.seth(0)  

    turtle.seth(-90)

    turtle.down()

    turtle.fd(60)

    turtle.goto(x, y)

    turtle.right(60)

    turtle.fd(20)

    turtle.left(90)

    turtle.fd(10)

    turtle.left(120)

    turtle.fd(20)

    turtle.up()

    turtle.goto(x, y)

    turtle.seth(0)  

    turtle.seth(-115)

    turtle.down()

    turtle.fd(25)

    turtle.up()

    turtle.goto(x, y)

    turtle.seth(0)  

    turtle.seth(-10)

    turtle.down()

    turtle.fd(20)

    turtle.right(90)

    turtle.fd(8)

    turtle.right(120)

    turtle.fd(20)

    turtle.goto(x, y)

    turtle.seth(-60)

    turtle.fd(20)

    turtle.up()

 

 

for x, y in x_y:

    draw_flower(x, y)

 



turtle.up()

turtle.goto(-200, -50)

turtle.down()

turtle.seth(0)   

turtle.seth(45)

turtle.fd(40)

turtle.begin_poly()  

x, y = turtle.get_poly()[0]  

turtle.right(90)

turtle.fd(35)

turtle.goto(x, y)

turtle.left(135)

turtle.fd(90)

turtle.seth(0)

turtle.circle(30)  

turtle.goto(x, y + 60)  

turtle.fd(40)

turtle.circle(30, 70)  

turtle.seth(0)

turtle.up()

turtle.goto(x, y + 50)  

turtle.down()

turtle.fd(50)

turtle.begin_poly()  

f_x, f_y = turtle.get_poly()[0]

 



turtle.up()

turtle.goto(x - 15, y + 120)  

turtle.down()

turtle.pensize(4)

turtle.seth(45)

turtle.circle(-10, 70)  

turtle.dot(10)  

turtle.up()

 

turtle.goto(x + 10, y + 120)  

turtle.down()

turtle.pensize(4)

turtle.seth(45)

turtle.circle(-10, 70)  

turtle.dot(10)  

turtle.up()

 



turtle.goto(x, y + 105)  

turtle.down()

turtle.circle(10, 70)  

 



turtle.pensize(3)  

turtle.up()

turtle.goto(f_x, f_y)  

turtle.left(20)

turtle.down()

turtle.fd(60)

turtle.pensize(2)  

turtle.begin_poly()  

x, y = turtle.get_poly()[0]

turtle.backward(80)

turtle.up()

turtle.goto(x, y)

turtle.down()

turtle.right(90)

turtle.fd(20)

turtle.right(90)

turtle.fd(8)

turtle.right(120)

turtle.fd(25)

turtle.right(200)

turtle.fd(25)

turtle.up()

turtle.goto(x, y)

turtle.down()

turtle.right(60)

turtle.fd(25)

turtle.goto(x, y)

turtle.right(40)

turtle.fd(25)

turtle.left(90)

turtle.fd(8)

turtle.left(110)

turtle.fd(25)

 

turtle.goto(f_x + 34, f_y + 75)

draw_heart(8, angle=20)  

 



turtle.up()

turtle.goto(150, 200)

turtle.pencolor("PINK")  

turtle.write('HAPPY VIETNAMESE', font=("Times New Roman", 30, "bold"))

turtle.goto(180,140)

turtle.write('WOMEN DAY 20-10', font=("Times New Roman", 30, "bold"))

 

turtle.hideturtle()

turtle.mainloop()