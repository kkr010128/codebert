h, n, *a = map(int, open(0).read().split())
print(["No", "Yes"][h <= sum(a)])