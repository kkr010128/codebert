n, k, s = map(int, input().split())

ans = []
for i in range(k):
    ans.append(s)
    
if s == 10 ** 9:
    out_of_s = 1
else:
    out_of_s = s + 1

for i in range(n - k):
    ans.append(out_of_s)
    
for a in ans:
    print(a, end=' ')