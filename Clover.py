#clover - Giáo Ộp IT
import turtle as T
import colorsys
T.Screen().bgcolor("black")
p=T.Turtle()
p.pensize(7)
p.speed(500)
p.goto(0,0)
h=0.8
def heart(angle, len=100):
    p.seth(angle)
    p.forward(len)
    p.circle(0.6*len,180)
    p.seth(angle-130)
    p.forward(1.55*len)
    p.seth(angle+100)
    p.forward(len)
    p.circle(-(0.6)*len,180)
    p.seth(angle-130)
    p.forward(1.55*len)
    p.pensize(7)

    

for i in range(50):
    c=colorsys.hsv_to_rgb(h,.8,1)
    p.pencolor(c)
    p.fillcolor(c)
    p.begin_fill()
    heart((i*90)-20,-i+200)
    p.end_fill()
    h+=0.03
p.penup()
p.goto(-280,-80)
p.pendown()
p.color("black")
p.write(" GOOD LUCKS!", font=("Arial",50,"bold"))
p.penup()
p.goto(-140,-120)
p.pendown()
p.color("blue")
p.write("* Giáo Ộp IT *", font=("Arial",30,"bold"))
p.penup()
T.done()

