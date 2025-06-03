a, b, m = map(int, input().split())
a_l = list(map(int, input().split()))
b_l =  list(map(int, input().split()))
x_y_c = [ list(map(int, input().split())) for _ in range(m) ]

ans = min(a_l) + min(b_l)
for x,y,c in x_y_c:
   ans = min(a_l[x-1]+b_l[y-1]-c, ans)
print(ans) 