K = int(input())
a = [0]
a[0] = 7 % K
for i in range(K):
    a.append((a[i]*10 + 7) % K)
    if a[i] == 0:
        print(i+1)
        exit()
print("-1")