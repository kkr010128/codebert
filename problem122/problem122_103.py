from collections import Counter
n = int(input())
A = list(map(int, input().split()))
q = int(input())
dict_A = Counter(A)
sum_list = sum(A)
for i in range(q):
    b, c = map(int, input().split())
    if b not in dict_A:
        print(sum_list)
    else:
        b_num = dict_A[b]
        dict_A[c] += dict_A[b]
        dict_A[b] = 0
        sum_list = sum_list + (c - b) * b_num
        print(sum_list)
