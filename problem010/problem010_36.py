n = raw_input()

A = map(int, raw_input().split())

for i, key in enumerate(A):

    j = i - 1

    while(j >= 0 and A[j] > key):
        A[j+1] = A[j]
        j -= 1

    A[j+1] = key

    for x in A:
        print x,
    print