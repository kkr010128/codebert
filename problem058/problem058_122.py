n = 0
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        for i in range(1, a+1):
            for j in range(1, i):
                for k in range(1, j):
                    if i + j + k == b:
                        n += 1
        print(n)
    n = 0
        
