from turtle import *


def rcurve():
    for i in range(80):

        # Defining step by step curve motion
        left(1)
        forward(1)


def lcurve():
    for i in range(80):

        # Defining step by step curve motion
        right(1)
        forward(1)


def rebcurve():
    for i in range(49):

        # Defining step by step curve motion
        right(1)
        forward(3)


def lebcurve():
    for i in range(49):

        # Defining step by step curve motion
        left(1)
        forward(3)


def rloweyecurve():
    for i in range(62):

        # Defining step by step curve motion
        left(1)
        forward(1)


def rloweyemidcurve():
    for i in range(39):

        # Defining step by step curve motion
        left(1)
        forward(2)


def lloweyecurve():
    for i in range(62):

        # Defining step by step curve motion
        right(1)
        forward(1)


def lloweyemidcurve():
    for i in range(39):

        # Defining step by step curve motion
        right(1)
        forward(2)


def luplipcurve():
    for i in range(30):

        # Defining step by step curve motion
        right(1)
        forward(1)


def ruplipcurve():
    for i in range(30):

        # Defining step by step curve motion
        left(1)
        forward(1)


def trirloweyecurve():
    for i in range(50):

        # Defining step by step curve motion
        left(1)
        forward(1)


def trirloweyemidcurve():
    for i in range(23):

        # Defining step by step curve motion
        left(1)
        forward(2)


def trilloweyecurve():
    for i in range(50):

        # Defining step by step curve motion
        right(1)
        forward(1)


def trilloweyemidcurve():
    for i in range(23):

        # Defining step by step curve motion
        right(1)
        forward(2)


def rsidemuk():
    for i in range(65):

        # Defining step by step curve motion
        left(1)
        forward(3)


def lsidemuk():
    for i in range(65):

        # Defining step by step curve motion
        right(1)
        forward(3)


def earringdes():
    for i in range(18):

        # Defining step by step curve motion
        circle(30)
        right(20)


def mukdes1():
    forward(30)
    for i in range(30):
        left(1)
        forward(1)
    circle(10, 210)


def mukdes2():
    forward(30)
    for i in range(30):
        right(1)
        forward(1)
    right(180)
    circle(10, -210)


def square(length, angle):
    for i in range(4):
        forward(length)
        right(angle)


def squarecircle():
    for i in range(15):
        square(20, 90)
        right(24)


def kolka():
    pensize(3)
    # left(180)
    forward(75)
    circle(20, 210)
    forward(75)
    left(158)
    forward(70)
    circle(10, 195)
    forward(70)


def squarecirclemuk():
    for i in range(15):
        square(40, 90)
        right(24)


def neclacedes1():
    for i in range(12):

        # Defining step by step curve motion
        circle(20)
        right(30)


pencolor('black')
pensize(3)
left(25)
circle(400, 50)
circle(400, -50)
right(50)
circle(400, -50)
right(255)
forward(250)
right(60)
forward(251)
left(90)
pencolor('white')
forward(20)
pencolor('black')
pensize(7)
left(90)
forward(260)
left(60)
forward(260)
right(90)
forward(40)
right(90)
forward(280)
right(60)
forward(280)
right(85)
forward(40)
up()
setpos(145, 295)
down()
pensize(3)
pencolor('black')
right(60)
forward(75)
rcurve()
forward(85)
up()
setpos(-145, 295)
down()
pencolor('black')
left(90)
forward(75)
lcurve()
pensize(3)
forward(85)
up()
setpos(12, 158)
down()
right(70)
circle(10, -230)
up()
setpos(-12, 158)
down()
left(180)
circle(10, 230)
right(120)
circle(10, 210)
up()

setpos(15, 152)
down()
right(220)
circle(30, -340)
up()
setpos(40, 245)
down()
left(115)
rebcurve()
up()
setpos(40, 245)
down()
right(45)
rloweyecurve()
rloweyemidcurve()
forward(25)
up()
setpos(-40, 245)
down()
left(115)
lebcurve()
up()
setpos(-40, 245)
down()
left(45)
lloweyecurve()
lloweyemidcurve()
forward(25)
up()

setpos(-97, 249)
down()
pensize(25)
circle(13)
up()
setpos(112, 251)
down()
circle(13)
up()
setpos(-35, 90)
pensize(3)
down()
right(105)
# forward(10)
luplipcurve()
right(55)
forward(11)
up()
setpos(35, 90)
down()
right(177)
# forward(10)
ruplipcurve()
left(60)
forward(11)
up()
setpos(-35, 90)
down()
left(70)
circle(38, 65)
up()
setpos(35, 90)
down()
left(60)
circle(38, -75)
up()
setpos(-35, 90)
down()
left(205)
circle(48, -45)
left(65)
circle(48, -40)
up()
setpos(-35, 90)
down()
pensize(6)
forward(10)
circle(2)
up()
setpos(35, 90)
down()
right(180)
forward(10)
circle(2)
up()
setpos(-10, 50)
down()
pensize(3)
left(8)
forward(20)
up()
setpos(0, 285)
down()
left(45)
trirloweyecurve()
trirloweyemidcurve()
up()
setpos(0, 285)
down()
left(15)
trilloweyecurve()
trilloweyemidcurve()
up()
setpos(0, 275)
down()
right(30)
circle(50, 60)
circle(50, -60)
right(60)
circle(50, -60)
up()
setpos(-5, 325)
down()
pensize(20)
circle(5)
up()
setpos(-3, 260)
down()
pensize(15)
circle(1)
up()
setpos(-285, 60)
down()
pensize(3)
right(10)
circle(80, -310)
right(180)
lsidemuk()
forward(20)
rsidemuk()
circle(30, -300)
right(180)
trilloweyecurve()
lsidemuk()
forward(15)
trirloweyemidcurve()
forward(22)
up()
setpos(285, 60)
down()
pensize(3)
right(180)
circle(80, 310)
rsidemuk()
forward(20)
lsidemuk()
right(180)
circle(30, 300)
trirloweyecurve()
rsidemuk()
forward(15)
trilloweyemidcurve()
forward(22)
up()
setpos(205, 45)
down()
pensize(2)
earringdes()
up()
setpos(-205, 45)
down()
pensize(2)
earringdes()
up()
pensize(3)
setpos(-290, 90)
down()
left(150)
# right(30)
mukdes1()
up()
setpos(-255, 155)
down()
left(180)
mukdes2()
up()
setpos(-265, 230)
down()
left(10)
mukdes1()
up()
setpos(-265, 310)
down()
pensize(8)
circle(3)
up()
setpos(-275, 335)
down()
pensize(8)
circle(2)
up()
setpos(-285, 355)
down()
pensize(8)
circle(1)
up()
setpos(-270, 165)
down()
pensize(8)
circle(1)
up()
setpos(-250, 235)
down()
pensize(8)
circle(1)
up()
pensize(3)
setpos(290, 90)
down()
left(180)
mukdes2()
up()
setpos(255, 155)
down()
left(10)
mukdes1()
up()
setpos(265, 230)
down()
left(170)
mukdes2()
up()
setpos(265, 310)
down()
pensize(8)
circle(3)
up()
setpos(275, 335)
down()
pensize(8)
circle(2)
up()
setpos(285, 355)
down()
pensize(8)
circle(1)
up()
setpos(270, 165)
down()
pensize(8)
circle(1)
up()
setpos(250, 235)
down()
pensize(8)
circle(1)
up()
setpos(-210, 298)
down()
pensize(4)
circle(9)
up()
setpos(-180, 315)
down()
pensize(4)
circle(9)
up()
setpos(-150, 331)
down()
pensize(4)
circle(9)
up()
setpos(-120, 348)
down()
pensize(4)
circle(9)
up()
setpos(-90, 365)
down()
pensize(4)
circle(9)
up()
setpos(-60, 382)
down()
pensize(4)
circle(9)
up()
setpos(-30, 400)
down()
pensize(4)
circle(9)
up()
setpos(215, 305)
down()
pensize(4)
circle(9)
up()
setpos(183, 323)
down()
pensize(4)
circle(9)
up()
setpos(152, 340)
down()
pensize(4)
circle(9)
up()
setpos(121, 358)
down()
pensize(4)
circle(9)
up()
setpos(90, 378)
down()
pensize(4)
circle(9)
up()
setpos(60, 395)
down()
pensize(4)
circle(9)
up()
setpos(30, 410)
down()
pensize(4)
circle(9)
up()
setpos(0, 420)
down()
pensize(4)
circle(9)
up()
setpos(-335, 360)
down()
pensize(1)
squarecircle()
up()
setpos(335, 360)
down()
pensize(1)
squarecircle()
up()

setpos(-277, 415)
down()
right(130)
kolka()
up()

setpos(277, 412)
down()
left(85)
kolka()
up()

setpos(-225, 445)
down()
right(133)
kolka()
up()


setpos(225, 443)
down()
left(87)
kolka()
up()

setpos(-170, 478)
down()
right(135)
kolka()
up()

setpos(170, 478)
down()
left(90)
kolka()
up()

setpos(-115, 510)
down()
right(140)
kolka()
up()

setpos(115, 510)
down()
left(95)
kolka()
up()


setpos(2, 520)
down()
# right(148)
squarecirclemuk()
up()


pensize(2)
setpos(0, -65)
down()
neclacedes1()
up()

pensize(1)
setpos(-100, -30)
down()
squarecircle()
up()

setpos(100, -30)
down()
squarecircle()
up()

pensize(3)
setpos(-277, 415)
down()
begin_fill()
circle(5)
end_fill()
up()

pensize(3)
setpos(-225, 445)
down()
begin_fill()
circle(5)
end_fill()
up()


pensize(3)
setpos(-170, 478)
down()
begin_fill()
circle(5)
end_fill()
up()

pensize(3)
setpos(-115, 510)
down()
begin_fill()
circle(5)
end_fill()
up()


pensize(3)
setpos(277, 415)
down()
begin_fill()
circle(-5)
end_fill()
up()

pensize(3)
setpos(225, 445)
down()
begin_fill()
circle(-5)
end_fill()
up()


pensize(3)
setpos(168, 478)
down()
begin_fill()
circle(-5)
end_fill()
up()

pensize(3)
setpos(113, 510)
down()
begin_fill()
circle(-5)
end_fill()
up()

pensize(3)
setpos(60, 125)
down()
begin_fill()
circle(-5)
end_fill()
up()


pensize(3)
setpos(70, 135)
down()
begin_fill()
circle(-5)
end_fill()
up()


pensize(3)
setpos(70, 122)
down()
begin_fill()
circle(-5)
end_fill()
up()


setpos(-150, -15)
down()
right(110)
forward(40)
up()


setpos(150, -15)
down()
right(90)
forward(40)
up()


setpos(-130, 20)
down()
left(100)
forward(40)
up()


setpos(130, 20)
down()
left(250)
forward(40)
up()


setpos(-100, -60)
down()
left(120)
forward(73)
up()


setpos(100, -60)
down()
right(130)
forward(70)
up()


setpos(-70, -25)
down()
left(125)
forward(40)
up()


setpos(70, -25)
down()
right(120)
forward(40)
up()


setpos(-200, 130)
down()
right(105)
forward(120)
# earchain()
# forward(10)
up()


setpos(200, 130)
down()
right(27)
forward(120)
# earchain()
up()


setpos(-230, 190)
down()
begin_fill()
right(20)
square(20, 90)
end_fill()
up()


setpos(210, 175)
down()
begin_fill()
left(60)
square(20, 90)
end_fill()
up()
