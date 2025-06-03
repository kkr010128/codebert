import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = II()
    aa = MII()
    q = II()
    bc = [MII() for _ in range(q)]
    sumv = sum(aa)
    numbers = [0]*(10**5+1)
    for a in aa:
        numbers[a] += 1

    for b,c in bc:
        numb = numbers[b]
        sumv += numb*(c-b)
        print(sumv)
        numbers[b] = 0
        numbers[c] += numb

if __name__ == '__main__':
    main()