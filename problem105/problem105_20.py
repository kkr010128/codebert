n = int(input())
a = map(int, input().split())
cnt = 0

for i, v in enumerate(a):
    if (i+1) % 2 == 1 and v % 2 == 1:
        cnt+=1
print(cnt) 