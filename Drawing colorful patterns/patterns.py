import turtle
colors=['red','yellow','blue','orange']
turtle.speed(0)
turtle.bgcolor('black')
for i in range(360):
  turtle.pencolor(colors[i% len(colors)])
  turtle.forward(i)
  turtle.right(121)
turtle.exitonclick()