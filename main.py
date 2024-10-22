import turtle

#Set up the turtle
star = turtle.Turtle()

#color
turtle.Screen().bgcolor("blue")
sc=turtle.Screen()
sc.setup(500,500)
turtle.title("STAR")



#Function to draw a star
def draw_star(size):
    for i in range(5):
        star.forward(size)
        star.right(144) #Turning angle for star points

#Set the star size
star_size = 100

#Draw the star
draw_star(star_size)

#Finish
turtle.done()