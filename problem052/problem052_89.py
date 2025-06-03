n = input()
out = ""
for i in range(1, int(n) + 1):
    if i % 3 == 0 or "3" in str(i):
        out += " " + str(i)
print(out)
