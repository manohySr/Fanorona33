grille = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

grilleIndex = [
    ['00', '01', '02'],
    ['10', '11', '12'],
    ['20', '21', '22']
]

def grilleView(grille):
    print('---------------------------------')
    print("Grille: \n")
    for i in grille:
        print('\t', i)
    print('---------------------------------')
    print('The index of the grille\n')
    for j in grilleIndex:
        print('\t', j)
    print('---------------------------------')

def isGrilleFull(grille):
    for g in grille:
        for cellule in g:
            if cellule == 'O':
                return False
    return True

class Player:
    def __init__(self, name, valueToMake):
        self.name = name
        self.valueToMake = valueToMake
        self.pionNumberIn = 0

    def getName(self):
        return self.name

    def makeFirstMove(self, grille):
        statePlayerMove = self.checkAllPlayerPionIn()
        if statePlayerMove == False:
            print(f"It's {self.name} turn")
            print("Put your pion in coordinate i and j")

            try:
                i = int(input("i coordinate to move is : "))
            except ValueError:
                print("Enter an integer value !!!")
                i = int(input("i coordinate to move is : "))
            try:
                j = int(input("j coordinate to move is : "))
            except ValueError:
                print("Enter an integer value !!!")
                j = int(input("j coordinate to move is : "))

            if grille[i][j] == self.valueToMake:
                return grille
            grille[i][j] = self.valueToMake
            self.pionNumberIn = self.pionNumberIn + 1
        return grille

    def checkAllPlayerPionIn(self):
        if self.pionNumberIn == 3:
            return True
        return False
    
    def movePion(self, grille, i, j, newI, newJ):
        statePlayerMove = self.checkAllPlayerPionIn()
        if statePlayerMove and grille[newI][newJ] == 'O':
            grille[i][j] = 'O'
            grille[newI][newJ] = self.valueToMake
            print(f'Pion in [{i},{j}] changed to [{newI},{newJ}]')
            return grille
        return grille

    """
    which position to place the pion
    00 01 02
    10 11 12
    20 21 22

    switch 
    if 00: can be moved in 01 10
    if 10: can be moved in 00 11 20
    if 20: ... 10 21

    if 01: ... 00 02 11
    if 11: ... 01 10 12
    if 21: ... 20 22 11

    if 02: ... 12 01
    if 12: ... 02 11 22
    if 22: ... 21 12
    """

    def whichMoveCanBeDone(self, i, j):
        if i == 0 and j == 0:
            print('Can be moved in i,j = (0,1) or (1,0)')
        if i == 1 and j == 0:
            print('Can be moved in i,j = (0,0) or (1,1) or (2,0)')
        if i == 2 and j == 0:
            print('Can be moved in i,j = (1,0) or (2,1)')

        if i == 0 and j == 1:
            print('Can be moved in i,j = (0,0) or (0,2) or (1,1)')
        if i == 1 and j == 1:
            print('Can be moved in i,j = (0,1) or (1,0) or (1,2)')
        if i == 2 and j == 1:
            print('Can be moved in i,j = (2,0) or (2,2) or (1,1)')

        if i == 0 and j == 2:
            print('Can be moved in i,j = (1,2) or (0,1)')
        if i == 1 and j == 2:
            print('Can be moved in i,j = (0,2) or (1,1) or (2,2)')
        if i == 2 and j == 2:
            print('Can be moved in i,j = (2,1) or (1,2)')


def playerActionForMoving(player, grille):
    name = player.getName()
    grilleView(grille)
    print(f"It's {name} turn")
    print("Put your pion in coordinate i and j")

    try:
        i = int(input("i coordinate to move is : "))
    except ValueError:
        print("Enter an integer value !!!")
        i = int(input("i coordinate to move is : "))

    try:
        j = int(input("j coordinate to move is : "))
    except ValueError:
        print("Enter an integer value !!!")
        j = int(input("j coordinate to move is : "))

    player.whichMoveCanBeDone(i, j)
    newI = int(input("Move to newI: "))
    newJ = int(input("Move to newJ: "))
    player.movePion(grille, i, j, newI, newJ)
    if grille[i][j] != 'O':
        playerActionForMoving(player, grille)
    grilleView(grille)
    return grille

def doYouWin(grille, player):
    tab = extractTab(grille)
    stateTab = 0
    for t in tab:
        for i in t:         
            if i == player.valueToMake:
                stateTab += 1
        if stateTab == 3:
            return [True, f'{player.name} is the winner !!!!']
        
    return [False, "Let's the game continue"]    


def extractTab(grille):
    """
    extract array to see if someone win the game

    which position win
    00 01 02
    10 11 12
    20 21 22

    00 10 20
    01 11 21 
    02 12 22

    00 11 22
    02 11 20
    """
    tab1 = grille[0]
    tab2 = grille[1]
    tab3 = grille[2]

    tab4 = []
    tab5 = []
    tab6 = []

    tab7 = [grille[0][0], grille[1][1], grille[2][2]]
    tab8 = [grille[0][2], grille[1][1], grille[2][0]]
    for i in grille:
        tab4.append(i[0])
        tab5.append(i[1])
        tab6.append(i[2])
        
    tab = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8]

    return tab


def startGame():
    p1 = input("Player 1, write your name: ")
    player1 = Player(p1, 'X')
    p2 = input("Player 2, write your name: ")
    player2 = Player(p2, 'M')
    print("Game begin \n")
    stateGame = True
    while stateGame == True:

        #check all player pion in before doing the game
        isPlayer1PionAllIn = player1.checkAllPlayerPionIn()
        isPlayer2PionAllIn = player2.checkAllPlayerPionIn()

        while isPlayer1PionAllIn == False and isPlayer2PionAllIn == False:
            grilleView(grille)
            player1.makeFirstMove(grille)
            grilleView(grille)
            player2.makeFirstMove(grille)

            isPlayer1PionAllIn = player1.checkAllPlayerPionIn()
            isPlayer2PionAllIn = player2.checkAllPlayerPionIn()
            if isPlayer1PionAllIn == True and isPlayer2PionAllIn == True:
                break

        result = doYouWin(grille, player1)
        if result[0] == True:
            print(result[1])
            break
        else:
            print(result[1])

        result = doYouWin(grille, player2)
        if result[0] == True:
            print(result[1])
            break
        else:
            print(result[1])

        playerActionForMoving(player1, grille) 
        result = doYouWin(grille, player1)
        if result[0] == True:
            print(result[1])
            break
        else:
            print(result[1])

        playerActionForMoving(player2, grille) 
        result = doYouWin(grille, player2)
        if result[0] == True:
            print(result[1])
            break
        else:
            print(result[1])

    print("Game over")

startGame()