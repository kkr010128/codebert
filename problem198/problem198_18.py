N = int(input())

alp = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
alp2 = "abcdefghij"

def solve(N):
    ans = []
    if N == 1:
        ans.append("a")
    else:
        pre = solve(N-1)
        for i in range(len(pre)):
            tmp = sorted(pre[i])
            num = alp[tmp[len(tmp)-1]]
            for j in range(num+1):
                ans.append(pre[i]+alp2[j])
    return ans
            

f_ans = solve(N)
f_ans.sort()

for i in range(len(f_ans)):
    print(f_ans[i])

