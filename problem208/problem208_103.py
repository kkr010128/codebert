n, m = map(int, input().split())

num = [-1 for _ in range(n)]

for _ in range(m):
    s, c = map(int, input().split())
    s -= 1

    if n >= 2 and s == 0 and c == 0:
        print(-1)
        exit()
    
    elif  num[s] != -1 and num[s] != c:
        print(-1)
        exit()
    else:
        num[s] = c

if num[0] == -1 and n != 1:
    num[0] = 1
elif num[0] == -1 and n == 1:
    num[0] = 0

num = ["0" if n == -1 else str(n) for n in num]

print("".join(num))