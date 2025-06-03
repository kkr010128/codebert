N = int(input())
A_list = list(map(int, input().split()))

if A_list[0] > 1:
    print(-1)
    exit()
elif A_list[0] == 1:
    if N == 0:
        print(1)
    else:
        print(-1)
    exit()


sumA = sum(A_list)
node = 1
count = 1
for i in range(len(A_list) - 1):
    temp = min([node * 2, sumA])
    count += temp
    node = temp - A_list[i + 1]

    if node < 0:
        print(-1)
        exit()

    sumA -= A_list[i + 1]

print(count)