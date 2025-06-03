ans = []
for s in open(0).readlines():
    if "?" in s:
        break
    ans.append(eval(s.strip().replace("/", "//")))
print(*ans, sep='\n')
