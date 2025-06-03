class dice:
    def __init__(self,label):
        self.top, self.front, self.right, self.left, self.rear, self.bottom \
                = label

    def roll(self,op):
        if   op=='N': self.top, self.front, self.bottom, self.rear = \
                                self.front, self.bottom, self.rear , self.top
        elif op=='E': self.top, self.left , self.bottom, self.right = \
                                self.left , self.bottom, self.right, self.top
        elif op=='W': self.top, self.right, self.bottom, self.left = \
                                self.right, self.bottom, self.left , self.top
        elif op=='S': self.top, self.rear , self.bottom, self.front = \
                                self.rear , self.bottom, self.front, self.top

    def print_top(self): print(self.top)
    def print_right(self): print(self.right)

    def get_label(self):
        return [self.top, self.front, self.right, self.left, self.rear, self.bottom]
 
label = list(map(int,input().split()))
d = dice(label)
q = int(input())
for _ in range(q):
    top_front = [int(x) for x in input().split()]
    for op in 'EEESSSWWWNNNWWWSSWWSESWS':
        if d.get_label()[:2] == top_front:
            d.print_right()
            break
        d.roll(op)