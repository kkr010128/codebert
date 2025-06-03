s = input()
t = input()
print(sum([1 for a,b in zip(list(s), list(t)) if a != b]))