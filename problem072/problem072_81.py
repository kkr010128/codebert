cnt = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        cnt += 1
    else:
        cnt = 0

    if cnt > 2:
        print("Yes")
        quit()
        
print("No")