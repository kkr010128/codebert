N = int(input())
S = input()
ret = ''
for s in S:
    o = ord(s) - ord('A') + N
    ret += chr(ord('A') + o % 26)
print(ret)