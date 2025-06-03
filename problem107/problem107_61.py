def pcmod(n):
    if n==0:
        return 1
    return 1+pcmod(n%bin(n).count('1'))

def main():
    n = int(input())
    x = list(map(int,list(input())))

    m_1 = x.count(1)-1
    m_0 = x.count(1)+1 
    baser_1 = 0
    baser_0 = 0
    if m_1!=0:
        for i in range(n):
            baser_1 += x[i] * pow(2,(n-1-i),m_1)
            baser_1 %= m_1
        
    for i in range(n):
        baser_0 += x[i] * pow(2,(n-1-i),m_0)
        baser_0 %= m_0

    ans = [0]*n

    for i in range(n):
        a = 0
        if x[i]==1:
            if m_1==0:
                ans[i] = 0
                continue
            t = (baser_1 - pow(2,(n-1-i),m_1))%m_1
            a = pcmod(t)

        if x[i]==0:
            t = (baser_0 + pow(2,(n-1-i),m_0))%m_0
            a = pcmod(t)
        ans[i] = a

    for a in ans:
        print(a)
if __name__ == "__main__":
    main()