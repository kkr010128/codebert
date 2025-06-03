N = int(input())
L = list(map(int, input().split()))

if N <= 2:
    print(0)
    exit()
    
count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            rod = [L[i], L[j], L[k]]
            condition = set(rod)
            rod = sorted(rod)
            if rod[0] + rod[1] > rod[2] and len(condition) == 3:
                count += 1
                
print(count)