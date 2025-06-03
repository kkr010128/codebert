N = int(input())

result = ["a"]
alph = "abcdefghijklmn"

def gen(w):
    ret = []
    s = len(set(w))
    for ch in alph[:s+1]:
        ret.append(w+ch)
    return ret

i = 0
w = result[i]
while len(w) <= N:
    w = result[i]
    result.extend(gen(w))
    i += 1
    if len(w) == N:
        print(w)
