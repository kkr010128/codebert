h1, m1, h2, m2, k = map(int, input().split())

s = h1*60+m1
t = h2*60+m2
ans = t-s-k
print (max(ans,0))