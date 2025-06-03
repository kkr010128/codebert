n = int(input())
A = list(map(int, input().split()))
q = int(input())

num_sum = sum(A)
B = [0]*(10**5+1)

for i in A:
    B[i] += 1


for i in range(q):
    b, c = map(int, input().split())
    B[c] += B[b]
    num_sum += (c-b)*B[b]
    B[b] = 0
    print(num_sum)
