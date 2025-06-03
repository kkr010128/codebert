N = int(input())
L = list(map(int, input().split()))

counter = 0
if N < 3:
    print(counter)
else:
    for x in range(0, N - 2):
        for y in range(x + 1, N):
            for z in range(y + 1, N):
                if L[x] != L[y] and L[x] != L[z] and L[y] != L[z]:
                    if L[x] + L[y] > L[z] and L[x] + L[z] > L[y] and L[y] + L[z] > L[x]:
                        counter += 1
    print(counter)

