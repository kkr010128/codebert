tmp = input().split(" ")
N = int(tmp[0])
K = int(tmp[1])
ary = list(map(lambda x: int(x), input().split(" ")))
ary.sort()

print(sum(ary[0:K]))