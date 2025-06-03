while True:
    a, b, c = map(int, input().split())
    if a >= 1 and a <= 10000:
        if b >= 1 and b <= 10000:
            if c >= 1 and c <= 10000:
                if a <= b:
                    break
                    
i = 0
for num in range(a, b+1):
    if c%num == 0:
        i += 1
print(i)
