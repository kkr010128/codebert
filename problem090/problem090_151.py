def resolve():
    s = input()
    if "RRR" in s:
        res = 3
    elif "RR" in s:
        res = 2
    elif "R" in s:
        res = 1
    else:
        res = 0
    print(res)
resolve()