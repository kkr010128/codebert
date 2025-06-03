def main():
    n = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A_max = A[-1]
    g = []
    table = [True]*(A_max+1)
    for i,a in enumerate(A):
        if table[a]:
            temp = a
            while A_max >= temp:
                table[temp] = False
                temp+=a
            if i==n-1 or a!=A[i+1]:
                g.append(a)
    print(len(g))
main()