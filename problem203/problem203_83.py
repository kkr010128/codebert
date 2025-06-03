A,B = map(int, input().split())

for X in range(1,1001):
    if (X*108//100-X)==A and (X*110//100-X)==B:
        print(X)
        exit()
print(-1)