_, K, *H = map(int, open(0).read().split())
print(len(tuple(filter(lambda h: h >= K, H))))