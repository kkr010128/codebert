A,B = list(map(int, input().split()))

list_A = []
list_B = []

for i in range(A):
    a = list(map(int, input().split()))
    list_A.append(a)

for i in range(B):
    b = int(input())
    list_B.append(b)

for i in list_A:
    output = []
    for (y,z) in zip(i,list_B):
        op = y*z
        output.append(op)
    sum_op = sum(output)
    print(sum_op)