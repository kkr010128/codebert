def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

if __name__ == '__main__':
    i = 0
    N = int(input())
    a = []
    for j in range(N):
        a.append(int(input()))
        if(is_prime(a[j])) == True:
            i += 1
    print(i)