S = input()
if S == "RRR":
    print(3)
elif S == "RRS" or S == "SRR":
    print(2)
elif "R" in S:
    print(1)
else:
    print(0)
