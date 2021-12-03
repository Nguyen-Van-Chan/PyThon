import turtle

 

turtle.setup(1200, 600)  # the window size

 

# draw the heart

 

 

turtle.color("black", "red")

turtle.pensize(2)

turtle.speed(10)

turtle.up()  # about the brush

turtle.goto(0, 50)

 

turtle.down()

 

 

def draw_heart(r, angle=45):

    """

    :param r: the radius of a heart circle

    :param angle: initial brush angle

    :return: returns the coordinates of the heart tip of the peach

    """

    turtle.begin_fill()  # start filling

    turtle.seth(0)

    turtle.seth(angle)  # set brush orientation

    turtle.circle(-r, 180)  # draw a semicircle counterclockwise

    turtle.fd(2 * r)  # to move forward

    turtle.begin_poly()  # record the position of the brush

    x, y = turtle.get_poly()[0]  # gets the position of the brush

    turtle.right(90)  # counterclockwise rotating brush

    turtle.fd(2 * r)  # to move forward

    turtle.circle(-r, 180)

    turtle.end_fill()  # fill the end

    return x, y

 

 

# draw the peach heart

x_y = []

start_x = 0

for _ in range(4):

    turtle.goto(start_x, 50)

    turtle.down()  # put down the pen

    x_y.append(draw_heart(8))

    start_x += 50

    turtle.up()  # about the brush

 

 

# painting leaves

def draw_flower(x, y):

    """

    draw the flower under the heart

    :param x: peach-centered x shaft

    :param y: peach-centered y shaft

    :return:

    """

    turtle.up()

    turtle.goto(x, y)

    turtle.seth(0)  # restore brush to right

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

    turtle.seth(0)  # restore brush to right

    turtle.seth(-115)

    turtle.down()

    turtle.fd(25)

    turtle.up()

    turtle.goto(x, y)

    turtle.seth(0)  # restore brush to right

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

 

# draw a worm

turtle.up()

turtle.goto(-200, -50)

turtle.down()

turtle.seth(0)  # restore brush to right , good direction control

turtle.seth(45)

turtle.fd(40)

turtle.begin_poly()  # record the position of the brush , the position of the foot fork

x, y = turtle.get_poly()[0]  # gets the position of the brush

turtle.right(90)

turtle.fd(35)

turtle.goto(x, y)

turtle.left(135)

turtle.fd(90)

turtle.seth(0)

turtle.circle(30)  # a circle

turtle.goto(x, y + 60)  # the position of the hand

turtle.fd(40)

turtle.circle(30, 70)  # a circle , take the radian of the flower hand

turtle.seth(0)

turtle.up()

turtle.goto(x, y + 50)  # the position of the hand

turtle.down()

turtle.fd(50)

turtle.begin_poly()  # note the position of the hand to be used later to draw the flower

f_x, f_y = turtle.get_poly()[0]

 

# eyes

turtle.up()

turtle.goto(x - 15, y + 120)  # eye position

turtle.down()

turtle.pensize(4)

turtle.seth(45)

turtle.circle(-10, 70)  # draw arc , take the radian of the flower hand

turtle.dot(10)  # eye circle

turtle.up()

 

turtle.goto(x + 10, y + 120)  # eye position

turtle.down()

turtle.pensize(4)

turtle.seth(45)

turtle.circle(-10, 70)  # draw arc , take the radian of the flower hand

turtle.dot(10)  # eyes    a circle

turtle.up()

 

# the mouth

turtle.goto(x, y + 105)  # eye position

turtle.down()

turtle.circle(10, 70)  # draw arc , take the radian of the flower hand

 

# the flowers and leaves in the picture

turtle.pensize(3)  # brush size

turtle.up()

turtle.goto(f_x, f_y)  # the position of the hand

turtle.left(20)

turtle.down()

turtle.fd(60)

turtle.pensize(2)  # turn down the paint

turtle.begin_poly()  # note the position of the hand to be used later to draw the flower

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

draw_heart(8, angle=20)  # heart in hand

 

# write a word

turtle.up()

turtle.goto(150, 200)

turtle.pencolor("PINK")  # the brush color

turtle.write("TO: all the classmates ", font=(" founder shuti ", 30, 'normal'))

turtle.goto(180,140)

turtle.write(" here's to you ", font=(" founder shuti ", 30, 'normal'))

 

turtle.hideturtle()

turtle.mainloop()