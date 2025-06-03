S = int(input())
h = S // (60 * 60)
m = (S % (60*60)) // 60
s = S % 60
# セパレータ(sep)は":" を用いる
print(h, m, s, sep=":")
