import sys
l=[0]*26
for h in sys.stdin:
    for i in h:
        k=ord(i.lower())
        if 96<k<123:l[k-97]+=1
for i in range(26):print chr(i+97),':',l[i]