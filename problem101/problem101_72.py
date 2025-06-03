A, B, C = map(int, input().split())
K = int(input())
cnt = 0

while A>=B:
    cnt+=1
    B*=2
while B>=C:
    cnt+=1
    C*=2
print("Yes" if cnt<=K else "No")
