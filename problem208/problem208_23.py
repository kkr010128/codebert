import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, readline().split())
if M == 0:
    print([0, 10, 100][N - 1])
    exit()
m = map(int, read().split())
S, C = zip(*zip(m, m))

def test(n):
    st = str(n)
    if len(st) != N:
        return False
    for i, c in zip(S, C):
        i -= 1
        if st[i] != str(c):
            return False
    return True

def main():
    for n in range(1000):
        if test(n):
            return n
    return -1

print(main())
