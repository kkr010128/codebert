N = int(input())
Alist = list(map(int, input().split()))
 
Alist = [[idx+1, a] for (idx, a) in enumerate(Alist)]
 
Alist.sort(key=lambda x:x[1])
 
ans = [str(a) for a, _ in Alist]
print(" ".join(ans))