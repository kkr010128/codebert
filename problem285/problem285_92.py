def r(i):
    indr = s.find('<', i)
    return indr - i if indr != -1 else n - i - 1
def l(i):
    indl = s.rfind('>', 0, i)
    return i - indl -1 if indl != -1 else i 
s = input()
n = len(s) + 1
print(sum([max(r(i), l(i)) for i in range(n)]))