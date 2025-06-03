K = int(input())
def check(k):
    aaa = 0
    prev = 7%k
    for i in range(0,k):
        aaa+=1
        if prev == 0:
            return(aaa)
        prev = (prev*10+7)%k
    return(-1)
print(check(K))