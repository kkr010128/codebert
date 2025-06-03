def is_p(s):
    return s == s[::-1]
s = input()
l = (len(s) - 1)//2
r = l + 1
print('Yes' if is_p(s) and is_p(s[:l]) and is_p(s[r:]) else 'No')