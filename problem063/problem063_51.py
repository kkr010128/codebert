from string import ascii_lowercase, ascii_uppercase
s = open(0).read()
ans = [0]*26
for c in s:
    i = ascii_lowercase.find(c)
    if i > -1:
        ans[i] += 1
    i = ascii_uppercase.find(c)
    if i > -1:
        ans[i] += 1
for c, t in zip(ascii_lowercase, ans):
    print("%s : %d" % (c, t))
