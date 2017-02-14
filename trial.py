import turtle
def smiley():
	t = turtle.Turtle()
	t.speed(100)
	t.penup()
	t.right(90)
	t.forward(50)
	t.right(180)
	t.goto(150,0)
	t.pendown()
	t.goto(150,0)
	t.color("black")
	t.begin_fill()
	t.circle(150)
	t.color("yellow")
	t.end_fill()
	t.penup()
	t.color("black")
	t.goto(-50, 50)
	t.pendown()
	t.dot(5)
	t.penup()
	t.goto(50, 50)
	t.pendown()
	t.dot(5)
	t.penup()
	t.goto(-77.5,-30)
	t.pendown()
	t.right(180)
	t.circle(75,180)
	t.penup()
	t.goto(500,500)

def frown():
	import turtle
	t = turtle.Turtle()
	t.speed(100)
	t.penup()
	t.right(90)
	t.forward(50)
	t.right(180)
	t.goto(150,0)
	t.pendown()
	t.goto(150,0)
	t.color("black")
	t.begin_fill()
	t.circle(150)
	t.color("yellow")
	t.end_fill()
	t.penup()
	t.color("black")
	t.goto(-50, 50)
	t.pendown()
	t.dot(5)
	t.penup()
	t.goto(50, 50)
	t.pendown()
	t.dot(5)
	t.penup()
	t.goto(77.5,-100)
	t.pendown()
	t.left(360)
	t.circle(75,180)
	t.penup()
	t.goto(500,500)
def passwordcheck(x):
	count = 0
	if x.lower() is not x and x.upper() is not x:
    	count = count + 1
	if "1" in x or "2" in x or "3" in x or "4" in x or "5" in x or "6" in x or "7" in x or "8" in x or "9" in x or "0" in x:
   		count = count + 1
	if "~" in x or "`" in x or "!" in x or "@" in x or "#" in x or "$" in x or "%" in x or "^" in x or "&" in x or "*" in x or ")" in x or "(" in x  or "-" in x or "_" in x or "+" in x or "=" in x or "{" in x or "}" in x or "|" in x or "[" in x or "]" in x or ";" in x or ":" in x or "'" in x or "<" in x or "," in x or ">" in x or "." in x or "?" in x or "/" in x:
    	count = count + 1
	if count == 3:
    	print("Strong")
		smiley()
	if count == 2:
    	print("Medium")
		smiley()
	if count == 1:
    	print("Weak")
		frown()
	if count == 0:
    	print("Very Weak")
		frown()
x = input("Password(8 characters):")
while len(x)<8 or len(x)>8:
    x = input("Please enter an 8 character password:")

passwordcheck(x)
