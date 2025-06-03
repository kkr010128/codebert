N, K = list(map(lambda n: int(n), input().split(" ")))
h = list(map(lambda x: int(x), input().split(" ")))
print(len(list(filter(lambda height: height >= K, h))))