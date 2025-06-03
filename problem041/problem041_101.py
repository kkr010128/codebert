in_str = raw_input().split()
num = []
for s in in_str:
    num.append(int(s))
if(num[0] < num[2] or num[1] < num[3] or num[2] < 0 or num[3] < 0):
    print "No"
elif(num[0] < num[2]+num[4] or num[1] < num[3]+num[4] or num[2]-num[4] < 0 or num[3]-num[4] < 0):
    print "No"
else:
    print "Yes"