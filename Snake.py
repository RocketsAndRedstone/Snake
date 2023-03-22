import turtle
import random

pencil = turtle.Turtle()
screen = turtle.Screen()
screen.setworldcoordinates(-95 , -95 , 95 , 95)
pencil.shape("square")
pencil.penup()
apple = turtle.Turtle()
apple.ht()
apple.penup()
apple.shape("circle")
apple.color("Red")
def main():
    playing = True
    tailCords = []
    colisionArea = 6
    colisionArea1 = 4
    score = 0
    position1 = (0 , 0)
    posinion2 = (0 , 0)
    position3 = (0 , 0)
    position4 = (0 , 0)
    timesMoved = 0
    screen.delay(50)
    applePlaced = False
    while playing == True:
        if applePlaced == False:
            applePosition = placeApple(tailCords)
            applePlaced = True  
        if (pencil.xcor() - colisionArea <= applePosition[0]) and (pencil.xcor() + colisionArea >= applePosition[0]) and (pencil.ycor() + colisionArea >= applePosition[1]) and (pencil.ycor() - colisionArea <= applePosition[1]):
            applePlaced = False
            score += 1
            tailCords.append(pencil.xcor())
            tailCords.append(pencil.ycor())
            pencil.fd(5)
            pencil.stamp()
        else:
            if timesMoved == 0:
                for i in range(3):
                    tailCords.append(pencil.xcor())
                    tailCords.append(pencil.ycor())
                    pencil.fd(5)
                    pencil.stamp()
                timesMoved += 1
            else:
                tailCords.append(pencil.xcor())
                tailCords.append(pencil.ycor())
                pencil.fd(5)
                for i in range(2):
                    del tailCords[0]
                pencil.stamp()
                pencil.clearstamps(1)        
        turtle.onkey(up , "w")
        turtle.onkey(left , "a")
        turtle.onkey(down , "s")
        turtle.onkey(right , "d")
        turtle.listen()
        for i in range(int((len(tailCords) / 2))):
            if (pencil.xcor() - colisionArea1 <= tailCords[i]) and (pencil.xcor() + colisionArea1 >= tailCords[i] and pencil.ycor() - colisionArea1 <= tailCords[i + 1]) and (pencil.ycor() + colisionArea1 >= tailCords[i + 1]):
                deathScreen(score)
                playing = False
        if pencil.xcor()>= 95 or pencil.xcor()<= -95 or pencil.ycor()<= -95 or pencil.ycor()>= 95:
            deathScreen(score)
            playing = False
                  
def placeApple(tailCords):
    apple.clearstamps(1)  
    appleSpotX = random.randint(-90 , 90)
    appleSpotY = random.randint(-90 , 90)
    apple.goto(appleSpotX , appleSpotY)
    apple.stamp()
    return appleSpotX , appleSpotY
        
def up():
    if pencil.heading() == 0 or pencil.heading() == 180:
        pencil.setheading(90)
    
def down():
    if pencil.heading() == 0 or pencil.heading() == 180:
        pencil.setheading(270)
    
def left():
    if pencil.heading() == 90 or pencil.heading() == 270:
        pencil.setheading(180)
    
def right():
    if pencil.heading() == 90 or pencil.heading() == 270:
        pencil.setheading(0)
    
def deathScreen(score):
    pencil.reset()
    pencil.ht()
    pencil.write(f"GAME OVER\nyou ate {score} apple(s)")
    turtle.done()    

main()