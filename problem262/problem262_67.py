N = int(input())
Assertions = []
ansnum = 0

for i in range(N):
    b = []
    n = int(input())
    for j in range(n):
        xi,yi = map(int,input().split())
        b.append([xi-1,yi])
    Assertions.append(b)

for i in range(2**N):
    select = []
    
    ans = [0 for _ in range(N)]
    index = []
    flag = True
    
    for j in range(N):
        if ((i >> j) & 1):
            select.append(Assertions[j])
            
            index.append(j)
            
            ans[j] = 1
            
    
    for idx in index:
        for Assert in Assertions[idx]:
            if ans[Assert[0]] != Assert[1]:
                flag = False
                break
    
    if flag:
        ansnum = max(ansnum,len(index))

print(ansnum)