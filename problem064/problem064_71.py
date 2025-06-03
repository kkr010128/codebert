s = str(raw_input())
p = str(raw_input())

i = 0
while(1):
    if i == len(s):
        print "No"
        break
    if i+len(p) >= len(s):
        str = s[i:len(s)] + s[0:len(p)-len(s[i:len(s)])]
    else:
        str = s[i:i+len(p)]
    if str == p:
        print "Yes"
        break
    else:
        i += 1