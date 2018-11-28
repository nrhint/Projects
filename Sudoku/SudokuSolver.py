##Nathan Hinton
##11/21/2018
##For solving Sudoku puzzles.
##
##Methods of solving the puzzle:
## (1): You can check each row colum and box for a number that can go there and than do that to each empty box until the puzzle is solved.
## (2): You can do a probobality on each box to see if the box can contain what numbers.
## Also you would be able to solve the puzzle box by box and then you can get the numbers solved in eacn box.
##

class Solver:
    def __init__(self, PuzzleFile):
        self.dat = self.readFile(PuzzleFile)
        self.rawList = self.dat.split('\n')
        self.tempList = []
        self.finalList = []
        for x in range(len(self.rawList)):
            self.finalList.append(self.rawList[x].split(' '))
            
        #print(self.finalList)
    def readFile(self, PuzzleFile):
        f = open(str(PuzzleFile), 'r')
        dat = f.read()
        f.close()
        #print(dat)
        lst = []
        tempLst = []
        return dat
    def returnCord(self, cord):
        temp = self.finalList[cord[0]]
        return temp[cord[1]]
    def returnBlanks(self):
        self.blanks = []
        for y in range(0, 9):
            row = self.finalList[y]
            for x in range(0, 9):
                if row[x] == '_':
                    self.blanks.append((y, x))
        return self.blanks
    def work(self):
        blanks = self.returnBlanks()
        for x in range(len(blanks)):
            #print(blanks[x])
            nums = self.findOptions(blanks[x])
            if len(nums) == 1:
                print(blanks[x], nums)
                self.write(blanks[x], nums)
            else:
                pass
    def returnRowNum(self, cord):
        nums = []
        lst = self.finalList[cord[0]]
        for x in range(0, 9):
            if lst[x] == '_':
                pass
            else:
                nums.append(lst[x])
        return nums
    def returnColNum(self, cord):
        nums = []
        for x in range(0, 9):
            lst = self.finalList[x]
            if lst[cord[1]] == '_':
                pass
            else:
                nums.append(lst[cord[1]])
        return nums
    def returnBox(self, cord):
        nums = []
        y = cord[0]//3*3
        x = cord[1]//3*3
        for a in range(0, 3):
            for b in range(0, 3):
                if self.returnCord((y+a, x+b)) == '_':
                    pass
                else:
                    nums.append(self.returnCord((y+a, x+b)))
                    #print(self.returnCord((y+a, x+b)))
        return nums
##    def findColoPos(self, cord, target):
##        for x in range(0, 9):
##            lst = self.finalList[x]
##            if lst[cord[1]] == '_':
##                pass
##            elif lst[cord[1]] == str(target):
##                return [cord[0], x]
    def cordCheck(self, cord, target):
        num = 0
        xCord = cord[1]//3*3
        yCord = cord[0]//3*3
        #Here is the colo check
        for x in range(0, 3):#Check each colum
            if str(target) in self.returnColNum(cord):
                #print("False colo")
                return False#If the target number is in the same colum than return False
            else:
                for y in range(0, 9):
                    if self.finalList[y][xCord+x] == str(target):#check if the number is in the left and right colum.
                        num += 1
        #Here is the row check:
        for y in range(0, 3):#Check the row
            if str(target) in self.returnRowNum(cord):
                #print("False row")
                return False#If the target number is in the same colum than return False
            else:
                for x in range(0, 9):
                    if self.finalList[yCord+y][x] == str(target):
                        num += 1
        if num == 4:
            self.write(cord, str(target))
    def coloCheck(self, cord, target):
        num = 0
        xCord = cord[1]//3*3
        print("colo: " + str(xCord))
        #print(xCord)
        #print(cord[1]%3)
        #print()
        for x in range(0, 3):
            #print(x)
            if x == cord[1]%3:
                if str(target) in self.returnColNum(cord):
                    #print("Same colum number found!!")
                    return False
                #print("colo " + str(cord[1]%3) + " Done")
            else:
                for y in range(0, 9):#Check to the right and to the left.  if the target is in both colums than return true and, I dont need to know the position of the numbers as long as I know that they are there.  Also make a row check which should be eaiser than the coloum check.
                    if self.finalList[y][xCord+x] == str(target):
                        #print(str(target)+" Found!")
                        num += 1
                    #print(self.finalList[x][xCord+1])
                #print("#######################")
        if num >= 2:
            return True
        else:
            return False
    def rowCheck(self, cord, target):
        num = 0
        yCord = cord[0]//3*3
        #print(yCord)
        #print(cord[0]%3)
        #print()
        for x in range(0, 3):
            #print(x)
            if x == cord[0]%3:
                if str(target) in self.returnRowNum(cord):
                    return False
                #print("row " + str(cord[0]%3) + " skipped")
            else:
                for y in range(0, 9):#Check to the right and to the left.  if the target is in both colums than return true and, I dont need to know the position of the numbers as long as I know that they are there.  Also make a row check which should be eaiser than the coloum check.
                    if self.finalList[yCord+x][y] == str(target):
                        #print(str(target)+" Found!")
                        num += 1
                    #print(self.finalList[x][xCord+1])
                #print("#######################")
        if num >= 2:
            return True
        else:
            return False
    def combine(self, row, col, box):
        return row+col+box
    def findOptions(self, cord):
        self.notNums = self.combine(self.returnRowNum(cord), self.returnColNum(cord), self.returnBox(cord))
        self.possibleNums = []
        for x in range(1, 10):
            #print(x)
            if str(x) in self.notNums:
                pass
            else:
                self.possibleNums.append(x)
        #print(self.possibleNums)
        #print(self.notNums)
        #print(cord)
        #print(self.possibleNums)
        return self.possibleNums
    def mode2(self, blanks):#Broken.  needs to be fixed.
        for x in range(len(blanks)):
            #print(blanks[x])
            for z in range(0, 9):
                a = self.coloCheck(blanks[x], z)
                b = self.rowCheck(blanks[x], z)
                if a  == b == True:
                    self.write(blanks[x], [z])
    def testMode2(self):
        blanks = self.returnBlanks()
        for x in range(len(blanks)):
            for n in range(1, 10):
                b = self.cordCheck(blanks[x], n)
    def write(self, cords, value):
        c = cords
        print()
        print("replacing:")
        print(cords)
        print(value)
        print()
        print(self.finalList[c[0]])
        self.finalList[c[0]][c[1]] = value
        print(self.finalList[c[0]])
         
    def solve(self):
        end = False
        mode = 2
        currNum = 0
        self.cord = (0, 0)
        for x in self.finalList:
            print(x)
        while end == False:
            input("Press return to loop again")
            blanks = self.returnBlanks()
            if mode == 1:
                print("Mode 1")
                self.work(blanks)
            if mode == 2:
                print("Mode 2")
                self.mode2
                currNum +=1
                
            if len(x)>len(blanks):
                x = blanks
            else:
                mode +=1
            if mode > 2:
                mode = 1
            print()
            print()
            print()
            print()
            print()
            for x in self.finalList:
                print(x)
            print()
            print()
            print()
            

PuzzleFile = 'SudokuFile'
solver = Solver(PuzzleFile)
dat = solver.readFile(PuzzleFile)
#solver.solve()#Comment to disable autorun
c = (4, 2)
def display():
    for x in range(0, 9):
        print(solver.finalList[x])
display()

#solver.mode2(solver.returnBlanks())
