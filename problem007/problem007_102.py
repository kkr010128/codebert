N = 44
F = [0]*(N+1)

def dynamic(n):
    if n == 0 or n == 1:
        return 1
    if F[n] != 0:
        return F[n]
    F[n] = dynamic(n - 1) + dynamic(n - 2)
    return F[n]

if __name__ == '__main__':
    n = int(raw_input())
    print(dynamic(n))