N = int(input())
S = list(input())

ans = []
for s in S:
    w = ord(s)+N
    if w <= 90:
        ans.append(chr(w))
    else:
        ans.append(chr(w-26))
print("".join(ans))