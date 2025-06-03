from math import log2,ceil
def main():
    A,B,C=map(int,input().split())
    K=int(input())
    if A<B<C:
        print("Yes")
    else:
        op=0
        if B<=A:
            val=ceil(log2(A/B))
            op+=val
            B<<=val
            if B==A:
                B*=2
                op+=1
        if C<=B:
            val=ceil(log2(B/C))
            op+=val
            C<<=val
            if C==B:
                C*=2
                op+=1
        if op<=K:
            print("Yes")
        else:
            print("No")
if __name__=='__main__':
    main()