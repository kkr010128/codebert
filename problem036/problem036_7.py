#reference : http://qiita.com/clarinet758/items/53e31ec10b873975438b
#reference : #1511943 Solution for ITP1_1_C: Rectangle by Signorte
# print "%d %d" % (s ,l) => ERROR

a, b = map(int, raw_input().split())

s = a * b
l = 2 * (a + b)

print "%s %s" % (str(s) ,str(l))