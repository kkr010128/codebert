# h, a = map(int, input().split())
# from collections import OrderedDict
# d = OrderedDict()
# a = list(input().split())
b = list(map(int, input().split()))
print("Yes" if len(set(b)) == 2 else "No")