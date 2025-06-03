import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(read())
lim = int(n ** 0.5)
fact = [1]
for i in range(2, lim + 1):
    if (n % i == 0):
        fact.append(i)
    else:
        pass

if (len(fact) == 1):
    ans = n - 1

else:
    tar = fact[-1]
    ans = tar + int(n // tar) - 2

print(ans)
