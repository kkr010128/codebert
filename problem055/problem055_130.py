A = [[[0 for i in range(10)] for i in range(3)] for i in range(4)]

info = int(input())
for i in range(info):
    b,f,r,v = [int(i) for i in input().split()]
    A[b-1][f-1][r-1] += v
    if A[b-1][f-1][r-1] < 0:
        A[b-1][f-1][r-1] = 0
    elif A[b-1][f-1][r-1] > 9:
        A[b-1][f-1][r-1] = 9

for i in range(3):
    print(' '+' '.join([str(i) for i in A[0][i]]))
print('#'*20)
for i in range(3):
    print(' '+' '.join([str(i) for i in A[1][i]]))
print('#'*20)
for i in range(3):
    print(' '+' '.join([str(i) for i in A[2][i]]))
print('#'*20)
for i in range(3):
    print(' '+' '.join([str(i) for i in A[3][i]]))