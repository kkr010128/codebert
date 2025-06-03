# ()の問題は折れ線で捉えると良い

N = int(input())
ls = [] # 増減が正のもの(0を含む)
rs = [] # 増減が負のもの

tot = 0
for i in range(N):
    s = input()
    h = 0
    b = 0
    for c in s:
        if c == "(":
            h += 1
        else:
            h -= 1
        b = min(b, h)
    if h >= 0:
        # 折れ線に対して上っていく奴ら
        ls.append([b, h])
    else:
        # 折れ線に対して下っていく奴ら
        # 右から(hから見るので、最下点は-hする)
        rs.append([b-h, -h])
    tot += h

ls.sort(key = lambda x:x[0], reverse=True)
rs.sort(key = lambda x:x[0], reverse=True)

def check(s):
    h = 0
    for p in s:
        if h+p[0] < 0:
            return False
        h += p[1]
    return True

if check(ls) and check(rs) and tot == 0:
    print("Yes")
else:
    print("No")