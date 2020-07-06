from graphics import *


class Spot:
    #hasCheck = False
    
    def __init__(self ,x1 ,y1 ,x2 ,y2 ,i ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.index = i
        self.height = 50
        self.width = 50
        self.hasCheck = True


class RedTeam:
    radius = 20
    numberAlive = 12 #starting from zero there will be eleven beginning pieces
    positions = []
    def __init__(self):
        numberAlive = 12
        numberDead = 0
        
        
    
    def initTeam(self,spot_instance, win):
        #positions = []
        #spot_instance
        c = Circle(Point(spot_instance.x1 + spot_instance.width/2, 
                         spot_instance.y1 - spot_instance.width/2), self.radius)
        c.setFill("Red")
        #c.draw(win)
        self.positions.append(spot_instance)
        #print(self.positions)
    
    
class Checker:
    def __init__(self,x, y, win,i,row):
        self.currentPosition = i
        self.radius = 20
        self.width = 25
        self.color = "Black"
        self.circ = Circle(Point(x + self.width, 
                         y - self.width), self.radius)  
        self.circ.setFill("Black")
        self.circ.draw(win)
        self.row = row
        self.isKing = False

class BlackTeam:
    radius = 20
    numberAlive = 12 #starting from zero there will be eleven beginning pieces
    positions = []
    def __init__(self):
        numberAlive = 12
        numberDead = 0
        
        
    
    def initTeam(self,spot_instance, win, realPieces, i):
        #positions = []
        #spot_instance
        #c = Circle(Point(spot_instance.x1 + spot_instance.width/2, 
                         #spot_instance.y1 - spot_instance.width/2), self.radius)
        #c.setFill("Black")
        #c.draw(win)
        if (i in (0,1,2,3)):
            row = 0
        elif(i in (4,5,6,7)):
            row = 1
        elif(i in (8,9,10,11)):
            row = 2
        
        c = Checker(spot_instance.x1, spot_instance.y1, win,i,row)
        self.positions.append(spot_instance)
        realPieces.append(c)
        #print(self.positions)
        
        


def printBoard(win, validSpots, spotsWithChecks, realPieces):
    board = Rectangle(Point(50,300), Point(450,700))
    board.setFill("Khaki")
    board.draw(win)
    
    
    initVals = [50,700,100,650]
    x1 = initVals[0]
    y1 = initVals[1]
    x2 = initVals[2]
    y2 = initVals[3]
    
    rows = 0
    
    for i in range (32):
        if(i % 4 == 0 and i != 0):
            rows = rows + 1
            if(rows%2 == 1):
                x1 = initVals[0] + 50
            elif(rows%2 == 0):
                x1 = initVals[0]
            y1 = initVals[1] - (50*rows)
            x2 = x1 + 50
            y2 = initVals[3] - (50*rows)
            
        sq = Rectangle(Point(x1,y1),Point(x2,y2))
        sq.setFill("Peru")
        sq.draw(win)
        #print(x1, y1, x2, y2)
        validSpots.append(Spot(x1,y1,x2,y2, i))
        x1 = x1 + 100
        x2 = x2 + 100
        
        
    
def initTeams(validSpots, win, spotsWithChecks, realPieces):
    #init the black team
    black_team = BlackTeam()
    
    for i in range(black_team.numberAlive):
        black_team.initTeam(validSpots[i], win, realPieces, i)
        spotsWithChecks.append(validSpots[i].index)
        if(i == 11):
            for i in range(12):
                continue
                #print("Black Position: ",black_team.positions[i].index)

           
    #init the red team
    red_team = RedTeam()
    for i in range(31, 19, -1):
        red_team.initTeam(validSpots[i], win)
        #spotsWithChecks.append(validSpots[i].index)
        if(i == 20):
            for i in range(12):
                continue
                #print("Red Position: ",red_team.positions[i].index)
        #print(i)
    
    return black_team, red_team;
    

def pickAValidSpot(validSpots, activeSpots, win):
    j_val = 100
    spotIsValid = False
    
    
    
    while(spotIsValid == False):
        #get mouse click
        mouseClick = win.getMouse()     # get a mouse click and coordinates
        x = mouseClick.getX()
        y = mouseClick.getY()        
        for j in range(len(validSpots)):
            if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
                if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                    print("YOU CLICKED ON SPOT: ", j)  
                    j_val = j  
                if((j_val in activeSpots) and ((j_val+5 not in activeSpots) or (j_val + 4 not in activeSpots))):
                    if(j_val != 7):
                        initMessageBox(win,"VALID")
                        spotIsValid = True
                        return j_val,x,y
                    elif(j_val == 7 and ( 11 not in activeSpots) ):
                        initMessageBox(win,"VALID")
                        spotIsValid = True
                        return j_val,x,y                        
                        
                
                else:
                    if(j_val in (4,5,6,7)):
                        initMessageBox(win, "INVALID: LOCKED IN")
                        #j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
                    else:
                        initMessageBox(win,"INVALID ")
                        #j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
                        
                        

def pickAValidDestination(validSpots, activeSpots, win, j_val):
    validDestination = False
    m_val = 100
    
        
    
    while(validDestination == False):
        mouseClick = win.getMouse()     # get a new mouse click and coordinates
        x_val = mouseClick.getX()
        y_val = mouseClick.getY()          
        for m in range(len(validSpots)):
            if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ):                    #if your mouse click is in a valid spot
                if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                    #for e in range(len(realPieces)):
                    #    if(m == realPieces[e].currentPosition
                    
                    print("YOUR GOING TO SPOT: ", m)  
                    m_val = m
                    
                    diff = m_val - j_val
                    print("HERE IS THE DIFF: ",diff)
                    if(diff > 5):
                        initMessageBox(win, "SERIOUS PROBLEM")
                        #pickAValidDestination(validSpots, activeSpots, win)
                        #gameOver = True
                        #return gameOver
                    elif(diff < 3):
                        initMessageBox(win, "THAT PIECE IS NOT A KING")
                    
                    elif(m_val in activeSpots):
                        initMessageBox(win, "THERE IS A PIECE ALREADY THERE")
                    
                        
                    else:
                        validDestination = True
                        initMessageBox(win, "VALID")
                        return m_val, x_val, y_val
                
            if(y_val < 300 or x_val > 450):
                goAhead = False    
    
def getRow(j_val):
    if(j_val in (0,1,2,3)):
        row = 0
    elif(j_val in (4,5,6,7)):
        row = 1
    elif(j_val in (8,9,10,11)):
        row = 2
    elif(j_val in (12,13,14,15)):
        row = 3
    elif(j_val in (16,17,18,19)):
        row = 4    
    elif(j_val in (20,21,22,23)):
        row = 5  
    elif(j_val in (24,25,26,27)):
        row = 6  
    elif(j_val in (28,29,30,31)):
        row = 7    
        
    return row
    

def checkSpot(validSpots, win):
    
    mouseClick = win.getMouse()     # get a mouse click and coordinates
    x = mouseClick.getX()
    y = mouseClick.getY()    
    
    #if j_val remains 1000 it means that the spot is invalid
    j_val = 1000
    
    for j in range(len(validSpots)):
        if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
            if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                print("YOU CLICKED ON SPOT: ", j)  
                j_val = j

    if(j_val == 1000):
        initMessageBox(win, "INVALID")
        return False, x, y
    else:
        return True, x, y
        
    
    
def go(win, validSpots, spotsWithChecks, realPieces, turns, pieceHistory, gameOver):
    
    
    spotIsValid = False
    
    finalRow = 7
    
    print("Enter go()")
    
    goAhead = True
    
    
    while (spotIsValid == False):
        spotIsValid, x, y = checkSpot(validSpots, win)
    
    m_val = 0
    j_val = 0
    
    
    activeSpots = []
    kingPins    = []
    for e in range(len(realPieces)):
        activeSpots.append(realPieces[e].currentPosition)
        if(realPieces[e].isKing == True):
            kingPins.append(e)
    
    print (activeSpots)
    print("HERE ARE THE KING PINS: ", kingPins)
    
    #for tomorrow Tam
    # if the turn is even then the update will be plus four
    # if the turn is odd then the update will be plus five
    
    theSpotYouPressed = 0
    
    for j in range(len(validSpots)):
        if(x > validSpots[j].x1 and x < validSpots[j].x2 ):                    #if your mouse click is in a valid spot
            if( y < validSpots[j].y1 and y > validSpots[j].y2):                
                print("YOU CLICKED ON SPOT: ", j)  
                j_val = j
                row = getRow(j_val)
            
                print ("ROW: ",row)
                if(row == 2):
                    print("KING")
                    initMessageBox(win,"THAT PIECE IS A KING")
                    
                initMessageBox(win, row)
                
             
    if(row % 2 == 1 ):   
        if(j_val == 7 and (11 in activeSpots) or (j_val == 15 and (19 in activeSpots))  or (j_val == 23 and (27 in activeSpots))):
            initMessageBox(win, "INVALID: LOCKED IN")
            j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)                
                
        elif((j_val in activeSpots) and ((j_val+5 not in activeSpots) or (j_val + 4 not in activeSpots))):
            initMessageBox(win,"VALID")        
        else:
            if(j_val in (4,5,6,7) or j_val in (12,13,14,16) or j_val in (20,21,22,23)):
                initMessageBox(win, "INVALID: LOCKED IN")
                j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
            else:
                initMessageBox(win,"INVALID ")
                j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)
    elif(row % 2 == 0):
        print("EVEN")
        if(j_val == 8 and (12 in activeSpots)):
            print("YESSS")
            initMessageBox(win, "INVALID")
        else:
            initMessageBox(win, "VALID")
            
    
    
    
        
    else:
        if(j_val in activeSpots):
            initMessageBox(win, "VALID")
        else:
            initMessageBox(win,"INVALID ")
            j_val, x, y = pickAValidSpot(validSpots, activeSpots, win)            
        
        
    #
    for k in range(len(realPieces)):
        if(j_val == realPieces[k].currentPosition):
            print("EUREKA", j_val, realPieces[k].currentPosition)
            k_val = k
    
    mouseClick = win.getMouse()     # get another mouse click and coordinates
    x_val = mouseClick.getX()
    y_val = mouseClick.getY()  
    
    for m in range(len(validSpots)):
        if(x_val > validSpots[m].x1 and x_val < validSpots[m].x2 ):                    #if your mouse click is in a valid spot
            if( y_val < validSpots[m].y1 and y_val > validSpots[m].y2): 
                #for e in range(len(realPieces)):
                #    if(m == realPieces[e].currentPosition
                    
                print("YOUR GOING TO SPOT: ", m)  
                m_val = m
                diff = m_val - j_val
                print("HERE IS THE DIFF: ",diff)
                if(diff > 5):
                    initMessageBox(win, "SERIOUS PROBLEM")
                    m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val)
                    #gameOver = True
                    #return gameOver
                elif(diff < 3):
                    initMessageBox(win, "THAT PIECE IS NOT A KING")
                    m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val) 
                elif(m_val in activeSpots):
                    initMessageBox(win, "THERE IS A PIECE ALREADY THERE")
                    m_val, x_val, y_val = pickAValidDestination(validSpots, activeSpots, win, j_val)
                    
                
                    
                                
                    
                
        if(y_val < 300 or x_val > 450):
            goAhead = False
    
                
                
        
                
    
    if(realPieces[k].currentPosition < len(validSpots)):
        if(x > validSpots[realPieces[k_val].currentPosition].x1 and x < validSpots[realPieces[k_val].currentPosition].x2 ):                    #if your mouse click is in a valid spot
            if( y < validSpots[realPieces[k_val].currentPosition].y1 and y > validSpots[realPieces[k_val].currentPosition].y2):
                #
                #print("YOUR CLICK IS IN A VALID SPOT 8!")
                if(x_val > x):
                    if(goAhead == True):
                        print("OLD POSITION: ", realPieces[k_val].currentPosition)
                        #move the checker to the right
                        realPieces[k_val].circ.move(50,-50)
                        #update the new position of the checker
                        realPieces[k_val].currentPosition = m_val
                        print("NEW POSITION: ", realPieces[k_val].currentPosition)
                    else:
                        initMessageBox(win,"ERROR DONT GO OFF THE BOARD")
                else:
                    if(goAhead == True):
                        print("OLD POSITION: ", realPieces[k_val].currentPosition)
                        #move the checker to the right
                        realPieces[k_val].circ.move(-50,-50)
                        #update the new position of the checker
                        realPieces[k_val].currentPosition = m_val
                        print("NEW POSITION: ", realPieces[k_val].currentPosition)
                    else:
                        initMessageBox(win,"ERROR DONT GO OFF THE BOARD") 
                        
    
    if(row == (finalRow-1)):
        print("KING")
        initMessageBox(win,"THAT PIECE IS A KING") 
        realPieces[k_val].isKing = True
                        
                        
                        
    return gameOver
                    
                        
                    
                    
                    
    
    
    
    #increment the place of the checker
    #if(turns == 0 or turns == 2):
    #    checker_place = checker_place + 4
    #elif(turns == 1):
    #    checker_place = checker_place + 5
        
    #print("UPDATE: ", checker_place)
                                
                                
                            
                            
                
     

def initMessageBox(win, strInput):
    board = Rectangle(Point(0,50), Point(500,200))
    board.setFill("white")
    board.draw(win)    
    message = Text(board.getCenter(), strInput)
    message.draw(win)
    

def main():
    
    spotsWithChecks = []
    realPieces = []
    pieceHistory = []
    turns = 0
    win = GraphWin("Checkers",800, 800)
    strInput = "Welcome to Checkers"
    initMessageBox(win,strInput)
    
    gameOver = False
    
    #this array will hold all of the valid spots a checker can be
    #in a checker board half of all squares are valid spots
    validSpots = [] #has all 32 valid spots
    
    #this function prints the board using the graphic library
    printBoard(win, validSpots, spotsWithChecks, realPieces)
       

    #the initTeams function draws the initial red and black checkers... 
    black_team, red_team = initTeams(validSpots, win, spotsWithChecks, realPieces)
    
    #the go function represents a players turn
    #right now it can tell if a spot has a checker
    iters = 0
    spotsWithChecks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    while (gameOver == False):
        gameOver = go(win, validSpots, spotsWithChecks, realPieces,turns, pieceHistory, gameOver)
        print ("The value of gameOver: ", gameOver)
        turns = turns + 1
    
    #print("There are", len(realPieces), "real pieces.")
    #print("There are", len(spotsWithChecks), "spots with checkers.")
    #print("There are", len(validSpots), "valid spots.")
    #print(spotsWithChecks)
    
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
