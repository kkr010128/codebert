import sys

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def main():
    A, B = map(int, input().split())

    pf_A = factorization(A)
    pf_B = factorization(B)

    if pf_A[0][0] == 1 or pf_B[0][0] == 1:
        pfs = []
    else:
        pfs = set([i for i,num in pf_A]) & set([i for i,num in pf_B])

    print(len(pfs)+1)
main()