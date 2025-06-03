m = 2000003

def MyHash(k,i):
    return (k%m+i*(1+(k%m)))%m

def main():
    n = input()
    T = ['']*2000003
    O = []
    for i in range(n):
        c, k = raw_input().split()
        i = 0
        if c == 'insert':
            k_hashed = hash(k)
            while True:
                j = MyHash(k_hashed,i)
                if T[j] == '':
                    T[j] = k
                    break
                else:
                    i += 1
        else:
            O.append(search(T,k))

    for item in O:
        print item

    return 0


def search(T,k):
    k_hashed = hash(k)
    i = 0
    while True:
        j = MyHash(k_hashed,i)
        if T[j] == k:
            o = 'yes'
            break
        elif T[j] == '':
            o = 'no'
            break
        else:
            i += 1

    return o


if __name__ == "__main__":
    main()