alp_count = [0]*26



string = open(0).read()
string = string.lower()


alp = [chr(ord("a")+i) for i in range(26)]

c = 0

for j in range(26):
    c = string.count(alp[j])
    alp_count[j] += c
    print("%s : %d"%(alp[j],alp_count[j]))
