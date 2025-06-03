A, B = map(int, input().split())
x = 0
while int(x * 0.08) <= A or int(x * 0.1) <= B:
    x += 1
    if int(x * 0.08) == A and int(x * 0.1) == B:
        print(x)
        exit()
print(-1)
