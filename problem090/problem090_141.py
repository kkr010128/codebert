s = input()
if s == "RRR":
    print(3)
elif s == "RRS" or s == "SRR":
    print(2)
elif s == "RSS" or s == "RSR" or s == "SRS" or s == "SSR":
    print(1)
else:
    print(0)
