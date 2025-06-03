class height():

    def __init__(self):
        self.human = 0
        self.step = 0

    def Sum(self):
        return self.human + self.step
N = int(input())
A = [height() for i in range(N)]

s = str(input()).split()

for i,v in enumerate(s):
    A[i].human = int(v)
    # print(i,v)

sum, tmp = 0,0
for i in range(len(A)-1):
    if A[i+1].human >= A[i].Sum():
        continue
    tmp = A[i].Sum() - A[i+1].human
    A[i+1].step = tmp
    sum += tmp

print(sum)
# for a in A:
#     print("human",a.human)