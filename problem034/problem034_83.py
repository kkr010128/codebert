class dice:
    def __init__(self,label):
        self.label = {i+1: l for i,l in enumerate(label)}
    def roll(self,op):
        l = self.label
        if   op=='N': self.label = {1:l[2], 2:l[6], 3:l[3], 4:l[4], 5:l[1], 6:l[5]}
        elif op=='E': self.label = {1:l[4], 2:l[2], 3:l[1], 4:l[6], 5:l[5], 6:l[3]}
        elif op=='W': self.label = {1:l[3], 2:l[2], 3:l[6], 4:l[1], 5:l[5], 6:l[4]}
        elif op=='S': self.label = {1:l[5], 2:l[1], 3:l[3], 4:l[4], 5:l[6], 6:l[2]}
    def yaw(self,op):
        l = self.label
        if   op=='CW' : self.label = {1:l[1], 2:l[3], 3:l[5], 4:l[2], 5:l[4], 6:l[6]}
        elif op=='CCW': self.label = {1:l[1], 2:l[4], 3:l[2], 4:l[5], 5:l[3], 6:l[6]}
    def get_label(self,i):
        return self.label[i]

if __name__ == '__main__':
    d0 = dice(list(map(int,input().split())))
    q = int(input())
    for _ in range(q):
        t,f = list(map(int,input().split()))
        for _ in range(3):
            if d0.get_label(1) == t: break
            d0.roll('E')
        if d0.get_label(1) != t:
            d0.roll('N')
            if d0.get_label(1) != t:
                for _ in range(2): d0.roll('N')
        if d0.get_label(2) != f:
            for _ in range(3):
                d0.yaw('CW')
                if d0.get_label(2) == f: break
        print(d0.get_label(3))