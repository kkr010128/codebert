n = int(raw_input())
print "",
for e in [i for i in range(1,n+1) if i%3==0 or str(i).count('3')>0]: print e,