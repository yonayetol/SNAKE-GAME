from turtle import *
from body_and_food_producer import *
import time
display=Screen()
display.bgcolor("black")
display.setup(600,600)
display.tracer(0)
body=[]
display.listen()
bon=The_Food()
# let's create some text to put high score
def original_body():
    for n in range(3):
        body.append(blen())
    q=Turtle("circle")
    q.up()
    q.color("white")
    q.goto(20,0)
    body.insert(0,q)
    for n in range(4):
        body[n].goto(x=((-n)*20),y=0)
    display.update()

def move_forward():
    for n in range(len(body),1,-1):
        x=body[n-2].position()
        body[n-1].goto(x)
    body[0].forward(20)
def move_up():
    if body[0].heading()!=270:
        for n in range(len(body),1,-1):
            x=body[n-2].position()
            body[n-1].goto(x)
        body[0].setheading(90)
        body[0].forward(20)
def move_down():
    if body[0].heading()!=90:
        for n in range(len(body),1,-1):
            x=body[n-2].position()
            body[n-1].goto(x)
        body[0].setheading(270)
        body[0].forward(20)
def move_right():
    if body[0].heading()!=180:
        for n in range(len(body),1,-1):
            x=body[n-2].position()
            body[n-1].goto(x)
        body[0].setheading(0)
        body[0].forward(20)
def move_left():
    if body[0].heading()!=0:
        for n in range(len(body),1,-1):
            x=body[n-2].position()
            body[n-1].goto(x)
        body[0].setheading(180)
        body[0].forward(20)
def eating_the_food_and_extending_the_snake():
    if the_food_list[0].distance(body[0])<20:
        the_food_list.clear()
        c=blen()
        x=body[-1].position()
        c.goto(x)
        body.append(c)
boy=Turtle()
def scoring():
    boy.up()
    boy.hideturtle()
    boy.color("white")
    boy.goto(-100,260)
    boy.write(f"score: {len(body)-3}",font=('Aerial',20,"bold"))
game_is_on=True
def ending():
    boom=Turtle()
    boom.up()
    boom.goto(-20,0)
    boom.hideturtle()
    boom.color("white")
    boom.write("GAME OVER!!!",font=("Aerial",30,"bold"))
original_body()
while game_is_on:
    time.sleep(0.81/(len(body)-3))
    tby=body[0].ycor()
    tbx=body[0].xcor()
    if tby>300:
        body[0].goto(tbx,-(tby)+5)
    if tby<-300:
        body[0].goto(tbx,-(tby)+5)
    if tbx>280:
        body[0].goto(-tbx+5,tby)
    if tbx<-280:
        body[0].goto(-tbx+5,tby)
    move_forward()
    
    display.onkey(fun=move_up,key="Up")
    display.onkey(fun=move_down,key="Down")
    display.onkey(fun=move_right,key="Right")
    display.onkey(fun=move_left,key="Left")
    bon.put_the_food_randomly()
    if the_food_list[0].distance(body[0])<20:
        boy.clear()
        scoring()
    eating_the_food_and_extending_the_snake()
      
    display.update()
    for n in body[2:]:  
        if body[0].distance(n)<20:
            ending()
            game_is_on=False
    display.update()

display.exitonclick()
