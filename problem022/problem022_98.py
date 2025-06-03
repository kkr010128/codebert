def LinearSearch(A,n,key):
    i = 0
    A[n] = key
    while A[i] != key:
        i += 1
    return i != n

N = int(input())
S = [int(x) for x in input().split(" ")]
S.append(None)


q = int(input())
T = [int(x) for x in input().split(" ")]

count = 0

for key in T:
    if LinearSearch(S,N,key):
        count += 1
print(count)
