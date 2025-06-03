__author__ = 'CIPHER'
_project_ = 'PythonLehr'

class BoundingBox:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def CalculateBox(self, x, y, r):
        if x>= r and x<=(self.width-r) and y>=r and y<=(self.height-r):
            print("Yes")
        else:
            print("No")
'''
width = int(input("Width of the Box: "))
height = int(input("Height of the Box: "))
x = int(input("location of x: "))
y = int(input("location of y: "))
r = int(input("radius of the circle; "))
'''

# alternative input
inputList = input()
inputList = inputList.split(' ')
inputList = [int(x) for x in inputList]
# print(inputList)
width = inputList[0]
height = inputList[1]
x = inputList[2]
y = inputList[3]
r = inputList[4]

Box = BoundingBox(width, height)
Box.CalculateBox(x, y, r)