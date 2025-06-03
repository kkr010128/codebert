def bunsan(n,S): #Sはリスト
    ave = sum(S)/n
    D = 0
    
    for i in range(n):
        D += (S[i] - ave)**2
    return (D/n)**(1/2)

while True:
    n = int(input())
    if n == 0:
        break
    S = list(map(int,input().split()))
    print(bunsan(n,S))
