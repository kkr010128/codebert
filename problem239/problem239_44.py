# ABC151
# A Next Alphabet
c = input()
l = [chr(ord("a")+i) for i in range(26)]
for i in range(26):
    if l[i] == c:
        print(l[i+1])
        break
