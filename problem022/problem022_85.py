def linearSearch(A, key):
    i = 0
    A.append(key)
    while A[i] != key:
        i += 1
    if i == len(A)-1:
        A.pop()
        return 'Not_found'
    A.pop()
    return i

if __name__ == '__main__':
    c = 0
    n = int(input())
    hoge1 = [int(x) for x in input().split()]
    q = int(input())
    for key in (int(x) for x in input().split()):
        if linearSearch(hoge1, key) == 'Not_found':
            continue
        else:
            c += 1
    print (c)
