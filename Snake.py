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
apple.color("Red")#creates the snake that you are controlling, the apple to be consumed, and the playing board
def main():
    playing = True
    tailCords = []
    colisionArea = 6
    colisionArea1 = 4#the area around the head of the snake where it will collide with itself or the apple
    score = 0
    timesMoved = 0
    screen.delay(50)#makes the turtle move at a reasonable speed
    applePlaced = False
    while playing == True:
        if applePlaced == False:#checks to see if there is an apple on the board, if not, one is placed
            applePosition = placeApple()
            applePlaced = True  
        if (pencil.xcor() - colisionArea <= applePosition[0]) and (pencil.xcor() + colisionArea >= applePosition[0]) and (pencil.ycor() + colisionArea >= applePosition[1]) and (pencil.ycor() - colisionArea <= applePosition[1]):
            applePlaced = False#detects to see if the head of the snake is within a set area around the apple
            score += 1
            tailCords.append(pencil.xcor())#used for the collision detection between the head and tail for the snake
            tailCords.append(pencil.ycor())
            pencil.fd(5)
            pencil.stamp()
        else:
            if timesMoved == 0:
                for i in range(3):#gives the snake its initial length so it is not just one segment long at the beginning
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
                    del tailCords[0]#removes the tail's coordinates for the segment that was just deleted on screen
                pencil.stamp()
                pencil.clearstamps(1)        
        turtle.onkey(up , "w")
        turtle.onkey(left , "a")
        turtle.onkey(down , "s")
        turtle.onkey(right , "d")
        turtle.listen()#gets the WASD input to control the snake
        for i in range(int((len(tailCords) / 2))):
            if (pencil.xcor() - colisionArea1 <= tailCords[i]) and (pencil.xcor() + colisionArea1 >= tailCords[i] and pencil.ycor() - colisionArea1 <= tailCords[i + 1]) and (pencil.ycor() + colisionArea1 >= tailCords[i + 1]):
                deathScreen(score)#Detects if the snake head has collided with any part of the tail, if so, it displays the amount of apples eaten
                playing = False
        if pencil.xcor()>= 95 or pencil.xcor()<= -95 or pencil.ycor()<= -95 or pencil.ycor()>= 95:#detects if the head of the snake has collided with any of the walls
            deathScreen(score)
            playing = False
                  
def placeApple():
    apple.clearstamps(1)#removes the previous apple so that it is fully consumed
    appleSpotX = random.randint(-90 , 90)
    appleSpotY = random.randint(-90 , 90)
    apple.goto(appleSpotX , appleSpotY)#generates and places the random spot for the apple
    apple.stamp()
    return appleSpotX , appleSpotY
        
def up():
    if pencil.heading() == 0 or pencil.heading() == 180:
        pencil.setheading(90)#makes the turtle face up if and only if it is not facing up or down already
    
def down():
    if pencil.heading() == 0 or pencil.heading() == 180:
        pencil.setheading(270)#makes the turtle face down if and only if it is not facing up or down already
    
def left():
    if pencil.heading() == 90 or pencil.heading() == 270:
        pencil.setheading(180)#makes the turtle face left if and only if it is not facing left or right already
    
def right():
    if pencil.heading() == 90 or pencil.heading() == 270:
        pencil.setheading(0)#makes the turtle face right if and only if it is not facing left or right already
    
def deathScreen(score):
    pencil.reset()
    pencil.ht()
    pencil.write(f"GAME OVER\nyou ate {score} apple(s)")
    turtle.done()#ends the game by clearing the board of the snake and displaying how many apples the player ate during the game    

main()
