def myfindall(s,ps):
    # start = 0
    matchlist =[]
    while True:
        tmp = s.find(ps)
        if tmp < 0 :
            break
        if len(matchlist)>0:
            matchlist.append(tmp+matchlist[-1]+1)
        else:
            matchlist.append(tmp)
        s = s[tmp+1:]
    return matchlist

instr = raw_input()
findstr = raw_input()
matchlist = myfindall(instr,findstr[0])
matchflag = False
y=0
for x in matchlist:
    if matchflag:
        break
    while True:
        if y >= len(findstr):
            print "Yes"
            matchflag = True
            break
        if x >= len(instr):
            x = 0
        if instr[x]==findstr[y]:
            x+=1
            y+=1
        else:
            y=0
            break
if not matchflag:
    print "No"