n = int(input())
t = 0
h = 0
for _ in range(n):
    a_lst = input().rstrip().split(" ")
    #print(a_lst)
    b_lst = sorted(a_lst)
    #print(b_lst)
    if a_lst[0] == a_lst[1]:
        t += 1
        h += 1
    elif a_lst == b_lst:
        h += 3
    else:
        t += 3
print(t, h)
