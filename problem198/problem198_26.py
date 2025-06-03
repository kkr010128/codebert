n = int(input())

def calc(x_list):
    tmp  = []
    for x in x_list:
        m = max(x)
        for alpha in range(ord('a'), ord(m) + 2):
            tmp.append(x + chr(alpha))
    if len(tmp[-1]) < n:
        tmp = calc(tmp)
    return tmp

ans = calc(['a'])
ans.sort()
if n >= 2:
    print(*ans, sep="\n")
else:
    print('a')