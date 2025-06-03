class Dice:
    top = 0
    def __init__(self,one,two,three,four,five,six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def role(self,direction):
        global top
        if(direction == 'S'):
                t1 = self.one
                self.one = self.five
                t2 = self.two
                self.two = t1
                t3 = self.six
                self.six = t2
                t4 = self.five
                self.five = t3
                top = self.one
       
        if(direction == 'E'):
            t1 = self.one
            self.one = self.four
            t2 = self.three
            self.three = t1
            t3 = self.six
            self.six = t2
            self.four = t3
            top = self.one
        if(direction == 'N'):
            t1 = self.one
            t2 = self.two
            t5 = self.five
            t6 = self.six
            self.one = t2
            self.two = t6
            self.six = t5
            self.five = t1
            top = self.one
        if(direction == 'W'):
            t1 = self.one
            t3 = self.three
            t4 = self.four
            t6 = self.six
            self.one = t3
            self.four = t1
            self.six = t4
            self.three = t6
            top = self.one
            
        return(top)
arr = [int(i) for i in input().split()]
op = str(input())
final = 0
a = Dice(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])
for i in range(len(op)):
     final = a.role(op[i])
print(final)

