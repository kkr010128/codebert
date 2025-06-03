import sys,collections
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
Ac = collections.Counter(A)

def num_combi2(n):
    combi = n*(n-1)//2
    return combi

def sub_combi2(n):
    c_before = n*(n-1)//2
    c_after =(n-1)*(n-2)//2
    return c_after - c_before

all_combi = 0
for val in Ac.values():
    all_combi += num_combi2(val)

for i in range(N):
    print(all_combi + sub_combi2(Ac[A[i]]))
