N = int(input())
Count = 0
for T in range(1,N+1):
    if not (T%3==0 or T%5==0):
        Count = Count+T
print(Count)