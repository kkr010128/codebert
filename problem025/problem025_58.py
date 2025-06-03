sum = 1
input()
for i in map(int,input().split()):
    sum|=sum<<i
input()
for j in map(int,input().split()):
    print(['no','yes'][(sum>>j)&1])
