from sys import exit

N, K = [int(x) for x in input().split()]
H = list([int(x) for x in input().split()])

if len(H) <= K:
    print(0)
    exit()

H.sort(reverse=True)
H = H[K:]

print(sum(H))
