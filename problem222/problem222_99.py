N = int(input())

A_list = list(map(int, input().split()))
A_list_min = sorted(A_list)

for i in range(len(A_list)-1):
    if A_list_min[i] == A_list_min[i+1]:
        print("NO")
        exit()
print("YES")