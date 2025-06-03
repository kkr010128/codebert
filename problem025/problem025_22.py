n = int(input())
A = [int(j) for j in input().split()]
q = int(input())
m = [int(j) for j in input().split()]
total = []
for i in range(2**n):
    bag = []
    for j in range(n):
        if ((i>>j)&1):
            bag.append(A[j])
    total.append(sum(bag))

for m1 in m:
    if m1 in set(total):
        print('yes')
    else:
        print('no') 
