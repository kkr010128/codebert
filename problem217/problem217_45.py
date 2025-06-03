N = int(input())

A_list = list(map(int, input().split()))

for i in range(N):
    if A_list[i] % 2 == 0:
        if A_list[i] % 3 == 0 or A_list[i] % 5 == 0:
            continue
        else:
            print("DENIED")
            exit()

if i == N-1:
    print("APPROVED")
