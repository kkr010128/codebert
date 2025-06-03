n = int(raw_input())
ls = []
for i in range(3,n+1):
    if i%3==0 or "3" in str(i) :
		ls.append(i)
print " " + " ".join(map(str,ls))