import tkinter as tk
import math
from tkinter import messagebox

def createGame():
    global game,boardY0,boardY1,boardY2,playerTurn,player1,player2,circle1,circle2,cross1,cross2
    

    boardY0 = list(["","",""])
    boardY1 = list(["","",""])
    boardY2 = list(["","",""])

    playerTurn = 2 # Turn 1 = X Turn 2 = O
    game.create_line(200,100,200,400,width=5)
    game.create_line(300,100,300,400,width=5)
    game.create_line(100,200,400,200,width=5)
    game.create_line(100,300,400,300,width=5)
    cross1=game.create_line(0,0,0,0,fill="red",width=0)
    cross2=game.create_line(0,0,0,0,fill="red",width=0)
    circle1=game.create_oval(0,0,0,0,fill="blue",width=5)
    circle2=game.create_oval(0,0,0,0,fill="blue",width=5)
    player1 = tk.Label(game, text = "Player One (X)", font = ("Arial",12 ), bg="Red")
    player2=tk.Label(game,text="Player Two (O)", font = ("Arial",12 ), bg="Blue")
    player1.place(x=175,y=20,anchor='n')
    player2.place(x=300,y=20,anchor='n')

def winnerDefined(winner):
    tk.messagebox.showinfo(title="The winner is...", message=f"{winner} is the winning symbol")  
    game.delete("all")
    createGame()
    switchTurn()

def checkWin():
    if len(set(boardY0)) == 1 and boardY0[0] !="": # top line horizontal
        return boardY0[0]
    elif len(set(boardY1)) == 1 and boardY1[0] !="": # middle line horizontal
        return boardY1[0]
    elif len(set(boardY2)) == 1 and boardY2[0] !="": # bottom line horizontal
        return boardY2[0]
    elif boardY0[0]==boardY1[0] and boardY1[0] == boardY2[0] and boardY1[0] !="": # left line vertical
        return boardY1[0]
    elif boardY0[1]==boardY1[1] and boardY1[1] == boardY2[1] and boardY1[1] !="": # middle line vertical
        return boardY1[1]
    elif boardY0[2]==boardY1[2] and boardY1[2] == boardY2[2] and boardY1[2] !="": # right line vertical
        return boardY1[2]
    elif boardY0[0]==boardY1[1] and boardY1[1] == boardY2[2] and boardY1[1] !="": # top left to bottom right
        return boardY0[0]
    elif boardY0[2]==boardY1[1] and boardY1[1] == boardY2[0] and boardY2[0] !="": # top right to bottom left
        return boardY2[0]

def gridAddX(pos): #Adding the x on the array
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    if y == 0:
        boardY0[x] = "x" 
    elif y == 1:
        boardY1[x] = "x"
    elif y == 2:
        boardY2[x] = "x"
        
def gridAddO(pos):
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    if y == 0:
        boardY0[x] = "o" 
    elif y == 1:
        boardY1[x] = "o"
    elif y == 2:
        boardY2[x] = "o"
        
def gridCheck(pos): #Checks whether something else in this position
    x,y = displayMouse(pos.x,pos.y)
    y = int(str(y)[0])-1
    x = int(str(x)[0])-1
    if y == 0:
        if boardY0[x] != "":
            return False
        else:
            return True
    elif y == 1:
        if boardY1[x] != "":
            return False
        else:
            return True
    elif y == 2:
        if boardY2[x] != "":
            return False
        else:
            return True
    
def clickX(pos): #Places the x on the grid
    global board
    tempx,tempy = displayMouse(pos.x,pos.y) #returns the gird position of the mouse
    if gridCheck(pos):
        gridAddX(pos)
        game.create_line(tempx-25,tempy-25,tempx+25,tempy+25,fill="red",width=5) #permenantely places the cross on that spot
        game.create_line(tempx+25,tempy-25,tempx-25,tempy+25,fill="red",width=5)
        switchTurn()
    
def clickO(pos):
    global board
    tempx,tempy = displayMouse(pos.x,pos.y)
    if gridCheck(pos):
        gridAddO(pos)
        game.create_oval(tempx-25,tempy-25,tempx+25,tempy+25,outline="blue",width=5)
        game.create_oval(tempx+25,tempy-25,tempx-25,tempy+25,outline="blue",width=5)
        switchTurn()
    
def click(pos): #run when left clicked, and runs the function for placing the object
    global playerTurn
    if playerTurn == 1:
        clickX(pos)
    elif playerTurn == 2:
        clickO(pos)
    if checkWin() != None:
        winnerDefined(checkWin())
        
def switchTurn(): # switches turn between players
    global playerTurn,player1,player2
    
    if playerTurn == 1:
        playerTurn=2
        player1.destroy()
        player2.destroy()
        player1 = tk.Label(game, text = "Player One (X)", font = ("Arial",12 ), bg="Red")
        player2=tk.Label(game,text="Player Two (O)", font = ("Arial",12 ), bg="Blue",fg="white")
        player1.place(x=175,y=20,anchor='n')
        player2.place(x=300,y=20,anchor='n')
    elif playerTurn == 2:
        playerTurn=1
        player1.destroy()
        player2.destroy()
        player1 = tk.Label(game, text = "Player One (X)", font = ("Arial",12 ), bg="Red",fg="white")
        player2=tk.Label(game,text="Player Two (O)", font = ("Arial",12 ), bg="Blue")
        player1.place(x=175,y=20,anchor='n')
        player2.place(x=300,y=20,anchor='n')
        
def displayO(x,y): #Deletes previous x and spawns a new one
    global circle1,circle2
    game.delete(circle1)
    game.delete(circle2)   
    circle1=game.create_oval(x-25,y-25,x+25,y+25,outline="blue",width=5)
    circle2=game.create_oval(x+25,y-25,x-25,y+25,outline="blue",width=5)
    
def displayX(x,y): #Deletes previous x and spawns a new one
    global cross1,cross2
    game.delete(cross1)
    game.delete(cross2)   
    cross1=game.create_line(x-25,y-25,x+25,y+25,fill="red",width=5)
    cross2=game.create_line(x+25,y-25,x-25,y+25,fill="red",width=5)       
     
        
def displayMouse(x,y): #Finds the square that the cursor is in
    global playerTurn
    tempx=0
    tempy=0
    change = False
    x = ((math.ceil(x/100))*100) - 50
    y = ((math.ceil(y/100))*100) - 50
    if tempx==0:
        tempx=x
        tempy=y
        if playerTurn == 1:
            displayX(tempx,tempy)
        elif playerTurn == 2:
            displayO(tempx,tempy)
    if x != tempx:
        tempx=x
        change = True
    if y!= tempy:
        tempy=x
        change = True
    if change == True:
        if playerTurn == 1:
            displayX(tempx,tempy)
        elif playerTurn == 2:
            displayO(tempx,tempy)
    return tempx,tempy
    
def callback(e): #Finds the mouse position at all times (e = info on mouse position)
    x= e.x
    y= e.y
    if x > 100 and x < 400 and y > 100 and y < 400:
        displayMouse(x,y)
    
root = tk.Tk() #root screen
root.geometry("500x500")
root.configure(bg="green")

game = tk.Canvas(root, width=500,height=500,bg="green") # canvas for the game 
game.pack()

createGame()
switchTurn()

game.bind("<Button-1>",click) # listening for mouse click
game.bind('<Motion>',callback) #listening for mouse movement
game.mainloop()