nag = int(input())

def dfs(rootlist,deep,n):
    global nag
    if len(rootlist) != nag:
        for i in range(n+1):
            nextroot = rootlist[:]
            nextroot.append(i)
            if i < n:
                dfs(nextroot,deep+1,n)
            else:
                dfs(nextroot,deep+1,n+1)
    else:
        answer = ''
        wordlist = ['a','b','c','d','e','f','g','h','i','j']
        for index in rootlist:
            answer += wordlist[index]
        print(answer)


dfs([0],0,1)
