class Dice():

    def __init__(self, nums):
        self.__indexTop__ = 1
        self.__indexFront__ = 2
        self.__indexRight__ = 3
        self.__indexLeft__ = 4
        self.__indexBack__ = 5
        self.__indexBottom__ = 6
        self.__sides__ = {1:nums[0], 2:nums[1], 3:nums[2], 4:nums[3], 5:nums[4], 6:nums[5]}
    
    def getTopSideNum(self):
        return self.__sides__[self.__indexTop__]
    
    def getFrontSideNum(self):
        return self.__sides__[self.__indexFront__]
        
    def getRightSideNum(self):
        return self.__sides__[self.__indexRight__]
    
    def roll(self, direction):
        initTop = self.__indexTop__
        initFront = self.__indexFront__
        initRight = self.__indexRight__
        initLeft = self.__indexLeft__
        initBack = self.__indexBack__
        initBottom = self.__indexBottom__
        if direction == 'N':
            self.__indexTop__ = initFront
            self.__indexFront__ = initBottom
            self.__indexRight__ = initRight
            self.__indexLeft__ = initLeft
            self.__indexBack__ = initTop
            self.__indexBottom__ = initBack
        elif direction == 'E':
            self.__indexTop__ = initLeft
            self.__indexFront__ = initFront
            self.__indexRight__ = initTop
            self.__indexLeft__ = initBottom
            self.__indexBack__ = initBack
            self.__indexBottom__ = initRight
        elif direction == 'S':
            self.__indexTop__ = initBack
            self.__indexFront__ = initTop
            self.__indexRight__ = initRight
            self.__indexLeft__ = initLeft
            self.__indexBack__ = initBottom
            self.__indexBottom__ = initFront
        elif direction == 'W':
            self.__indexTop__ = initRight
            self.__indexFront__ = initFront
            self.__indexRight__ = initBottom
            self.__indexLeft__ = initTop
            self.__indexBack__ = initBack
            self.__indexBottom__ = initLeft
    
    def pivot(self, direction):
        initTop = self.__indexTop__
        initFront = self.__indexFront__
        initRight = self.__indexRight__
        initLeft = self.__indexLeft__
        initBack = self.__indexBack__
        initBottom = self.__indexBottom__
        if direction == 'C':
            self.__indexTop__ = initTop
            self.__indexFront__ = initRight
            self.__indexRight__ = initBack
            self.__indexLeft__ = initFront
            self.__indexBack__ = initLeft
            self.__indexBottom__ = initBottom
        elif direction == 'CC':
            self.__indexTop__ = initTop
            self.__indexFront__ = initLeft
            self.__indexRight__ = initFront
            self.__indexLeft__ = initBack
            self.__indexBack__ = initRight
            self.__indexBottom__ = initBottom

die = Dice([int(i) for i in input().split()])
q = int(input())
for i in range(q):
    top, front = (int(i) for i in input().split())
    while True:
        if die.getTopSideNum() == top:
            break
        die.roll('N')
        if die.getTopSideNum() == top:
            break
        die.roll('W')
    while True:
        if die.getFrontSideNum() == front:
            break
        die.pivot('C')
    print(die.getRightSideNum())


