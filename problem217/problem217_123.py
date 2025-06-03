N = int(input())
anser = 'APPROVED'
A_list = list(map(int, input().split()))
for A in A_list:
    if A % 2 == 1:
        continue
    if A % 3 == 0:
        continue
    if A % 5 == 0:
        continue
    anser = 'DENIED'
    break
print(anser)