from sys import stdin

def main():
    for l in stdin:
        n, x = map(int, l.split(' '))
        if 0 == n == x:
            break

        print(len(num_sets(n, x)))

def num_sets(n, x):
    num_sets = []

    for i in range(1, n-1):
        for j in [m for m in range(i+1, n)]:
            k = x - (i+j)

            if n < k:
                continue

            if k <= j:
                break

            num_sets.append((i, j, k))

    return num_sets

if __name__ == '__main__': main()