from turtle import Turtle as trtl
Kirby = trtl()
Kirby.hideturtle()
Kirby.penup()
Kirby.setpos(-200,200)
Kirby.pendown()
Kirby.pos()
side = 10
Kirby.speed(0)
#color pixel method
def square(color):
    Kirby.color(color)
    Kirby.begin_fill()
    for i in range(4):
        Kirby.forward(side)
        Kirby.right(90)
        i=i
    Kirby.end_fill()
    Kirby.forward(side)
    
#next row method, doing rows from top to bottom
def nextRow(numSquares):
    Kirby.penup()
    Kirby.back(numSquares * side)
    Kirby.right(90)
    Kirby.forward(side)
    Kirby.left(90)
    Kirby.pendown()
    
# prints the row of pixels that color
def row(colors,numbers):
    numsquares = 0
    for i in range(len(colors)):
        for i2 in range(numbers[i]):
            square(colors[i])
            i2=i2
        numsquares += numbers[i]
    nextRow(numsquares) # reset the cursor
    
# colors we have
# colors = ["white" ,"black", "pink", "deeppink"]
pink = "#ff92c6"
darkpink = "#B54365"
brownpink = "#620f0b"
lightpink = "#ff1784"
darkbrownpink = "#64100e"
cherry = "#b50029"
hazepink = "#ffa2de"
midpink = '#f771a5'
redpink = '#de4973'

# row 1
colors = ["white", "black"]
numbers = [7, 6]
row(colors,numbers)
# row 2 [b,b,b,bp,dp,dp,bp,b,b,b]
colors = ["white", "black", brownpink, darkpink, brownpink, "black", "white"]
numbers = [ 5, 3, 1, 2, 1, 3, 1]
row(colors,numbers)
# row 3 bppbppppppppbwww
colors = ['white', "black", midpink, pink, hazepink, pink, redpink, "black", "white"]
numbers = [ 4, 2, 1, 1, 4, 1, 1, 2, 1]
row(colors,numbers)
# row 4 bpppppbpbppppbww
colors = ['white', "black", pink, hazepink, pink, darkbrownpink, "black", "white"]
numbers = [ 3, 2, 1, 8, 1, 1, 1, 1]
row(colors,numbers)
# row 5

row(colors,numbers)
# row 6 bpppppbpbpppppbw
colors = ["black", pink, "black", pink, "black", pink, "black", "white"]
numbers = [ 1, 5, 1, 1, 1, 5, 1, 1]
row(colors,numbers)
# row 7 bpppddpppddppppb
colors = ["black", pink, darkpink, pink, darkpink, pink, "black"]
numbers = [ 1, 3, 2, 3, 2, 4, 1]
row(colors,numbers)
# row 8 bppppppbpppppppb
colors = ["black", pink, "black", pink, "black"]
numbers = [ 1, 6, 1, 7, 1]
row(colors,numbers)
# row 9 wbpppppbpppppppb
colors = ["white", "black", pink, "black", pink, "black"]
numbers = [ 1, 1, 5, 1, 7, 1]
row(colors,numbers)
# row 10 wbppppppppppbbbw
colors = ["white", "black", pink, "black", "white"]
numbers = [ 1, 1, 10, 3, 1]
row(colors,numbers)
# row 11 wbpppppppppbdddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 1, 1, 9, 1, 3, 1]
row(colors,numbers)
# row 12 wwbpppppppbddddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 2, 1, 7, 1, 4, 1]
row(colors,numbers)
# row 13  wwbbppppppbddddb
colors = ["white", "black", pink, "black", darkpink, "black"]
numbers = [ 2, 2, 6, 1, 4, 1]
row(colors,numbers)
# row 14 wbddbbpppbddddbw
colors = ["white", "black", darkpink, "black", pink, "black", darkpink, "black", "white"]
numbers = [ 1, 1, 2, 2, 3, 1, 4, 1, 1]
row(colors,numbers)
# row 15 bdddddbbbbbddbww
colors = ["black", darkpink, "black", darkpink, "black", "white"]
numbers = [ 1, 5, 5, 2, 1, 2]
row(colors,numbers)
# row 16 wbbbbbbwwwbbbwww
colors = ["white", "black", "white", "black", "white"]
numbers = [ 1, 6, 3, 3, 3]
row(colors,numbers)

