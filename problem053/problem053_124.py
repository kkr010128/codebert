n=int(input())
list=list(map(int,input().split(" ")))
list.reverse()
for i in range(n-1):
    print(str(list[i])+" ",end="")
print(str(list[n-1]))
