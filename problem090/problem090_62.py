W = input()

if W.count("R") > 0:
    if W == "RRR":
        print(3)
    elif "RR" in W:
        print(2)
    else:
        print(1)
else:
    print(0)