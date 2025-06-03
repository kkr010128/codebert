H = int(input())
cnt = 1

while(H > 0):
    cnt *= 2
    H //= 2

print(cnt - 1)