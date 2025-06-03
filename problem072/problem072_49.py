n = int(input())
cnt = 0
judge = False
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
       cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        judge = True
if judge:
    print("Yes")
else:
    print("No")