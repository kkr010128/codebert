H, N = map(int, input().split())
list_A = list(map(int,input().split()))
sum_list_A = sum(list_A)
if sum_list_A >= H:
    print("Yes")
else:
    print("No")