class Dice1():
    def move(self,direction,n):
        if direction == "S":
            top = n[0]
            n[0] = n[4]
            n[4] = n[5]
            n[5] = n[1]
            n[1] = top
        elif direction == "N":
            top = n[0]
            n[0] = n[1]
            n[1] = n[5]
            n[5] = n[4]
            n[4] = top
        elif direction == "E":
            top = n[0]
            n[0] = n[3]
            n[3] = n[5]
            n[5] = n[2]
            n[2] = top
        elif direction == "W":
            top = n[0]
            n[0] = n[2]
            n[2] = n[5]
            n[5] = n[3]
            n[3] = top
        return n
n = [int(i) for i in input().split()]
di = list(input())
dc = Dice1()
for i in di:
    n = dc.move(i,n)
print(n[0])
