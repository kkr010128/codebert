
n = int(input())
cnt = 0
d1, d2 = [0] * n, [0] * n
for i in range(n):
    d1[i], d2[i] = map(int, input().split())

for i in range(n):
    if d1[i] == d2[i]:
        cnt += 1
    else:
        cnt = 0
    
    if cnt == 3:
        print("Yes")
        exit()
print("No")