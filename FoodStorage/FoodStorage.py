##Nathan Hinton
##For the food storage
##11/13/2018

#Item format:
#[ItemName, Number]

import pickle#For saving

class FoodStorage:
    def __init__(self):
        print("Class FoodStorage inited")
        self.fileName = 'FoodStorage.dat'
        self.openFile('r')
        #self.dat = pickle.load(self.file)
        print(self.dat)
    def openFile(self, readWrite):
        try:
            if readWrite == 'r':
                self.file = open(self.fileName, 'rb')
                print("File opened for reading")
                self.dat = pickle.load(self.file)
            elif readWrite == 'w':
                self.file = open(self.fileName, 'wb')
                print("File opened for writing")
            else:
                print("Input error to openFile")
        except FileNotFoundError:
            self.file = open(self.fileName, 'wb')
    def saveFile(self):
        self.openFile('w')
        ##Write Data
        pickle.dump(self.dat, self.file)
        print("Writing data")
        self.file.close()
        print("file closed!")
        print()
    def addItem(self):
        item = self.input()
        x = self.findItem(item)
        if type(x) == int:
            self.dat[x][1]+=item[1]
            print(self.dat[x])
        else:
            self.dat.append(item)
    def removeItem(self):
        item = self.input()
        x = self.findItem(item)
        if type(x) == int:
            self.dat[x][1]-=item[1]
            if self.dat[x][1] == 0:
                #Remove the item
                self.dat.pop(x)
        else:
            pass
    def findItem(self, item):
        match = False
        for x in range(len(self.dat)):
            #print(self.dat[x])
            if item[0].lower() == self.dat[x][0].lower():
                print("MATCH!!!")
                match = True
                return x
        if match == False:
            return 'NoMatch'
    def input(self):
        self.item = input("Item Name: ")
        self.itemNum = int(input("Item Number: "))
        return [self.item, self.itemNum]
    def main(self):
        self.run = True
        while self.run == True:
            try:
                #print(self.dat)
                print()
                print("1:Find item")
                print("2:Add Item")
                print("3:remove")
                print("4:save")
                print("5:List Items")
                self.i = input()
                if self.i == '1':
                    item = [input("Item Name:  "), 0]
                    x = self.findItem(item)
                    if type(x) == int:
                        #self.dat[x]
                        print()
                        print(self.dat[x])
                    else:
                        print(self.dat[self.x])
                elif self.i == '2':
                    self.addItem()
                elif self.i == '3':
                    self.removeItem()
                elif self.i == '4':
                    self.saveFile()
                elif self.i == '5':
                    self.dat.sort()
                    print(self.dat)
                else:
                    print("Input error!")
            except KeyboardInterrupt:
                print("Ending self.main...")
                self.run = False

def repair():
    f = open('FoodStorage.dat', 'wb')
    pickle.dump([['Bacon', 5], ['Ham', 3]], f)
    f.close()

#repair()
f = FoodStorage()
#f.openFile('r')
#f.saveFile()
f.main()
