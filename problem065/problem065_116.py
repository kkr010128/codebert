w=raw_input().lower()
l=[]
while 1:
    s=raw_input()
    if s=="END_OF_TEXT": break
    l+=s.lower().split()
print l.count(w)