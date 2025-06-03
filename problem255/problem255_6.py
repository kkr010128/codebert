n = input()
a, b = input().split(" ")
output = ""
for s, t in zip(a, b):
    output += s
    output += t
print(output)