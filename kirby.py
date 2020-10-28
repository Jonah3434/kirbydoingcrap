import turtle as trtl
Kirby = trtl.Turtle()
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
brownpink = "#601010"
neonpink = "#FF1880"
darkbrownpink = "#64100e"
cherry = "#B0203F"
hazepink = "#FFA0DF"
midpink = '#F070A0'
redpink = '#DF4870'
bubblegum = '#FF90C0'
black = '#000000'
white = '#FFFFFF'

# row 1
colors = ["white", "black"]
numbers = [7, 8]
row(colors,numbers)

# row 2 
colors  = ["white", "black", brownpink, cherry, 'black', cherry, bubblegum, "black", cherry, redpink, 'black', "white"]
numbers = [ 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1]
row(colors,numbers)

# row 3 
colors = ['black', redpink, bubblegum, midpink, redpink, cherry, midpink, bubblegum, 'white', brownpink, hazepink, 'white', brownpink, midpink, bubblegum, hazepink, redpink, 'black']
numbers = [ 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
row(colors,numbers)

# row 4 
colors = ['black', redpink, bubblegum, hazepink, bubblegum, hazepink, neonpink, midpink, 'black', hazepink, midpink, 'black', neonpink, bubblegum, hazepink, 'black']
numbers = [ 1, 1, 1, 4, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
row(colors,numbers)

# row 5
colors  = ['black', redpink, bubblegum, hazepink, bubblegum, hazepink, midpink, 'black']
numbers = [ 1, 1, 1, 7, 1, 7, 1, 1]
row(colors,numbers)

# row 6 
colors = ['white', "black", redpink, midpink, bubblegum, hazepink, bubblegum, hazepink, bubblegum, hazepink, redpink, brownpink, cherry, hazepink, cherry, black]
numbers = [ 0  , 1, 1, 1, 1, 2, 1, 4, 1, 2, 1, 1, 1, 2, 1, 1]
row(colors,numbers)

# row 7 
colors  = ['white', "black", redpink, midpink, bubblegum, hazepink, bubblegum, midpink, brownpink, bubblegum, hazepink, midpink, black]
numbers = [ 1, 1, 1, 2, 1, 5, 2, 1, 3, 1, 1, 1 ,1]
row(colors,numbers)

# row 8
colors = [ white, "black", cherry, redpink, midpink, hazepink, midpink, redpink, brownpink, midpink, hazepink, midpink, black]
numbers = [ 2, 1, 1, 1, 1, 6, 1, 1, 3, 1, 1, 1, 1 ]
row(colors,numbers)
'''
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
'''

wn = trtl.Screen()
wn.mainloop()
