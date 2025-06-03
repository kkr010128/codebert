def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
cnt = 0

for _ in range(N):
    D1, D2 = MI()
    
    if D1 == D2:
        cnt += 1
    else:
        cnt = 0
    
    if cnt == 3:
        print("Yes")
        exit()
    
print("No")