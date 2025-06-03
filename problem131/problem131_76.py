a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())

a_t = t*v
b_t = t*w

if a_t >= b_t+abs(a-b):
    print('YES')
else:
    print('NO')
