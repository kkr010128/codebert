K = int(input())

ai_1 = 0
for i in range(K):
    ai = (10*ai_1 + 7)%K
    if ai==0:
        print(i+1)
        exit()
    ai_1 = ai

print("-1")

