N = int(input())
A = list(map(int,input().split())) + [0]
kabu = 0
money = 1000

for p in range(N):
    #株がない時
    if A[p] < A[p+1]:
        kabu += money//A[p]
        money -= (money//A[p])*A[p]
    
    #株があるとき
    if A[p] > A[p+1]:
        money += kabu*A[p]
        kabu = 0 
    #print(str(p+1) + "日目" + str(money) + "  " +str(kabu))

print(money)