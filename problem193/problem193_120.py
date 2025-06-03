import math

h,w,k = map(int,input().split())
s = [str(input()) for i in range(h)]
ans = h * w

if h == 1:
    print(math.ceil("1".count(s[0])/k))
    exit()

for i in range(2 ** (h-1)):
    ss = str(format(i,"b").zfill(h-1))
    cnt = 0
    zero = 0
    key = 1
    for j in range(len(ss)):
        if ss[j] == "0":
            zero += 1
    now = [0 for i in range(zero+1)]

    for j in range(w):
        next = []
        num = 0
        for n in range(h):
            if s[n][j] == "1":
                num += 1
            if num > k:
                key = 0
            if n < h-1 and ss[n] == "0":
                next.append(num)
                num = 0
        next.append(num)
        
        keykey = 1
        for n in range(zero+1):
            if keykey:
                if now[n] + next[n] > k:
                    now = next
                    cnt += 1
                    keykey = 0
                else:
                    now[n] += next[n]
                    
    if key:ans = min(ans,cnt+zero)
print(ans)
