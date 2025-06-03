sample = input()
res =[]

for s in sample:
    if s.lower() == s:
        res.append(s.upper())
    elif s.upper() == s:
        res.append(s.lower())

print("".join(res))