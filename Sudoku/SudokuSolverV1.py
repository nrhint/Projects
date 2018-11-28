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
    def work(self, blanks):
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
    def write(self, cords, value):
        c = cords
        print()
        print("replacing:")
        print(cords)
        print(value)
        print()
        print(self.finalList[c[0]])
        self.finalList[c[0]][c[1]] = str(value)[1]
        print(self.finalList[c[0]])
         
    def solve(self):
        end = False
        self.cord = (0, 0)
        while end == False:
            input("Press return to loop again")
            blanks = self.returnBlanks()
            self.work(blanks)
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
solver.solve()
