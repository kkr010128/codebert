s = input()
if s == "RRR":
    x = 3
elif s == "RRS" or s == "SRR":
    x = 2
elif s == "SSS":
    x = 0
else:
    x = 1
print(x)