def get_input():
    while True:
        try:
            yield ''.join(raw_input().strip())
        except EOFError:
            break
inlist = list(get_input())
instr = "".join(inlist)
instr = instr.lower()
ascstart = 97
ascfin = 122
strlist = [0 for i in xrange(97,122+1)]
# print len(strlist)
for x in xrange(len(instr)):
    if ord(instr[x]) < ascstart or ord(instr[x]) > ascfin:
        continue
    strlist[ord(instr[x])-ascstart] +=1

for x in xrange(ascstart,ascfin+1):
    print "%s : %d" % (chr(x),strlist[x-ascstart])