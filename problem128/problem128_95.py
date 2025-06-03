#C
x, n = map(int, input().split())
if n ==0:
    print(x)
else:
    p = list(map(int, input().split()))
    num = list(range(-1, 102))

    num_removed=num
    for i in range(len(p)):
        num_removed=[num_removed for num_removed in num_removed if num_removed != p[i]]

    num_list=[]
    for i in num_removed:
        num_list.append(abs(x-i))

    min_index=min([i for i, j in enumerate(num_list) if j == min(num_list)])

    print(num_removed[min_index])