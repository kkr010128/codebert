def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
print(((1000-(n%1000))%1000 + 1000)%1000)
