import math , sys

N = int( input() )
A = list( map( int, input().split() ) )
Q = int( input() )

count = [0 for _ in range( 10**5 + 1)]

for each in A:
    count[each]+=1
ans = sum(A)
for _ in range(Q):
    B , C = list( map( int , input().split() ) )
    D = count[B]
    ans += (C-B) * D
    count[B] = 0
    count[C] += D
    print(ans)
