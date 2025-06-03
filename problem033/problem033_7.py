class Dice:
    D = {'E':(3,1,0,5,4,2), 'W':(2,1,5,0,4,3), 'S':(4,0,2,3,5,1), 'N':(1,5,2,3,0,4)}
    def __init__(self, tp, fwd, rs, ls, bk, bm):
        self.nbrs = [tp, fwd, rs, ls, bk, bm]
    def rll(self, drctn):
        return [self.nbrs[i] for i in self.D[drctn]]


A = input().split()
for i in input():
    dice = Dice(A[0], A[1], A[2], A[3], A[4], A[5])
    A = dice.rll(i)
print(A[0])
