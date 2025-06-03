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
def main3():
    n,m=map(int, input().split())
    k = factorization(n)
    k1 = factorization(m)

    y1 = set()
    y2 = set()

    for i in k:
        y1.add(i[0])
    for i in k1:
        y2.add(i[0])
    y1.add(1)
    y2.add(1)

    kouyaku = y1&y2
    print(len(kouyaku))



if __name__ == '__main__':
    main3()
