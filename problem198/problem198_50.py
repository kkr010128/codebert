n = int(input())

s = ['a']*(n)
#print(''.join(s))

def dfs(x,alp):
    if x == n:
        print(''.join(s))
        return
    
    for i in range(alp+1):
        #print(x,alp,i)
        s[x] = chr(i+ord("a"))
        dfs(x+1,max(i+1,alp))
        #print(alp)


dfs(0,0)