n = int(input())
alist = list(map(int,input().split()))
numb = [0]*n
for i in range(n):
    numb[alist[i]-1] = i+1
for i in range(n):
    print(numb[i],end=(' '))