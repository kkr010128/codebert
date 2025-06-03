import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N,A,B = LI()
if (A+B)%2==0:
    ans = (B-A)//2
else:
    count_move = min(A-1,N-B)
    ans = count_move+1
    ans += (B-A-1)//2
print(ans)
