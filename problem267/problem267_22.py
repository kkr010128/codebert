N = int(input())
S = input()
ans = 0
 
numlist = [str(i) for i in range(10)]
for a in numlist:
    idx_a = S.find(a)
    if idx_a == -1 or idx_a >= N - 2:
        continue
    
    for b in numlist:
        idx_b = S[idx_a+1:].find(b)
        if idx_b == -1 or idx_a + idx_b + 1 >= N - 1:
            continue
        
        for c in numlist:
            if c in S[idx_a + idx_b + 2:]:
                ans += 1
print(ans)