N = int(input())
A = [int(x) for x in input().split()]

if 0 in A :
    print("0")
    exit()
result = 1
for i in range(N) :
    result *= A[i]
    if result > 10**18 :
        print("-1")
        exit()

print(result)