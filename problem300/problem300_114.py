def main():

    def factorization(n):
        l = []
        tmp = n
        i = 2
        while i*i <= n:
            if tmp%i == 0:
                while tmp%i == 0:
                    tmp //= i
                l.append(i)
            i += 1
        if tmp != 1:
            l.append(tmp)
        if l == []:
            if n != 1:
                l.append(n)
        return l

    a, b = map(int, input().split())
    a_f = factorization(a)
    b_f = factorization(b)
    ans = len(set(a_f) & set(b_f)) + 1
    print(ans)
    
if __name__ == '__main__':
    main()