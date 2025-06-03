def main():
    n,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    """
    ruiseki = [1]
    for i in range(n):
        ruiseki.append(ruiseki[-1]*a[i])
    #ruiseki.pop(0)
    
    ans = [ruiseki[k]/ruiseki[0]]
    for i in range(k+1,n+1):
        tmp = ruiseki[i]/ruiseki[i-k]
        if ans[-1] >= tmp:
            print('No')
        else:
            print('Yes')
        ans.append(tmp)
    """
    for i in range(k,n):
        if a[i]>a[i-k]:
            print('Yes')
        else:
            print('No')
main()