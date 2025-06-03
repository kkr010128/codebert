import itertools

lst = list(map(int, input().split()))
k = int(input())

ans = 'No'
for tup in itertools.combinations_with_replacement([0, 1, 2], k):
    temp = lst[:]
    for i in tup:
        temp[i] *= 2
    if temp[0] < temp[1] and temp[1] < temp[2]:
        ans = 'Yes'
print(ans)