import collections
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = []
for _ in range(Q):
    query.append(tuple(map(int, input().split())))

dict_A = collections.Counter(A)
# print(dict_A)
ans = sum(A)
for i in range(Q):
    if query[i][0] in dict_A.keys():
        val = dict_A.pop(query[i][0])
        if query[i][1] in dict_A.keys():
            dict_A[query[i][1]] += val
        else:
            dict_A[query[i][1]] = val
        ans = ans - (val*query[i][0]) + (val*query[i][1])
    print(ans)
