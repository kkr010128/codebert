[N, K] = [int(i) for i in input().split()]
point_list = [int(i) for i in input().split()]

for i in range(N):
    if i >= K:
        if point_list[i-K] < point_list[i]:
            print("Yes")
        else:
            print("No")
