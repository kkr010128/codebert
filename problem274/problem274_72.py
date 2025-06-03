import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
s = input().rstrip()[::-1]

ans = []

left, right = 0, 0 + m

while True:
    if right >= n:
        ans.append(n - left)
        break
    for i in range(right, left, -1):
        flag = 1
        if s[i] == "0":
            ans.append(i - left)
            flag = 0
            break
    if flag:
        print(-1)
        sys.exit()
    else:
        left = i
        right = left + m

print(*ans[::-1])
        
        
