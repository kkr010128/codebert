n,k = map(int,input().split())
t = [1]*n
for i in range(k):
    input()
    for j in map(int,input().split()):
        t[j-1] = 0
print(sum(t))