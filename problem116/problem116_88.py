s = input()
t = input()

result = [x != y for x, y in zip(s, t)]
print(sum(result))