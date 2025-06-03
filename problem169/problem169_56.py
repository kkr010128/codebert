n = int(input())
ls = [0]*n
ls1 = list(map(int, input().split()))
for i in ls1:
    ls[i-1] += 1
for j in ls:
    print(j)