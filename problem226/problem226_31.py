h, _ = map(int, input().split())
a = list(map(int, input().split()))
print(["Yes", "No"][sum(a) < h])