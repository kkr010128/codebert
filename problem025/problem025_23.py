n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

# bit all search
pattern = []
for i in range(2 ** n):
    bit_set = []
    for j in range(n):
        if ((i >> j) & 1):
            bit_set.append(A[j])    
    pattern.append(sum(bit_set))

#print(pattern)  

for m in m:
    if m in pattern:
        print('yes')
    else:
        print('no')

