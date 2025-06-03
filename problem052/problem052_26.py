n = int(raw_input())

out = ""
for i in range(1, n + 1):
    if (i % 3 == 0) or (i % 10 == 3):
        out += " " + str(i)
        continue
    if "3" in str(i):
        out += " " + str(i)

print out