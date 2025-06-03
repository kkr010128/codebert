A, B, C = map(int, input().split())
K = int(input())
yes = False
for i in range(0, 8):
    for j in range(0, 8):
        for k in range(0, 8):
            if i + j + k == K:
                new_A = A * (2 ** i)
                new_B = B * (2 ** j)
                new_C = C * (2 ** k)
                if new_C > new_B and new_B > new_A:
                    yes = True
                    break
        if yes:
            break
    if yes:
        break
                
if yes:
    print("Yes")
else:
    print("No")