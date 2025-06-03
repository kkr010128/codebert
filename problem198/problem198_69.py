n = int(input())

w = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


s = {}
s["a"] = 0
ans = [s]

for i in range(2, n+1):
    new_s = {}
    for t in s.items():
        for j in range(1, i):
            if t[0][-1] == w[j-1]:
                for k in range(t[1] + 2):
                    new_s[t[0] + w[k]]  = max(t[1], k)

    ans.append(new_s)
    s = new_s

answer = sorted(ans[n-1].keys())

for x in answer:
    
    print(x) 
