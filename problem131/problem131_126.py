a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
d=abs(a-b)
u = v-w
if d-u*t<=0:
    print("YES")

else:
    print('NO')