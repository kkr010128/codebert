import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
X,Y,A,B,C = map(int,readline().split())
P = list(map(int,readline().split()))
Q = list(map(int,readline().split()))
R = list(map(int,readline().split()))
P = sorted(P,reverse=True)
Q = sorted(Q,reverse=True)
R = sorted(R,reverse=True)
P = P[:X]
Q = Q[:Y]
PQR = sorted(P+Q+R,reverse = True)
ans = sum(PQR[:X+Y])
print(ans)