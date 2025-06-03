def parseSpaceDivideIntArgs(arg):
    tmpArr = arg.split()
    ret = []
    for s in tmpArr:
        ret.append(int(s))
    return ret


instr = input()
# instr = "1 2 3"

instrSpl = parseSpaceDivideIntArgs(instr)
a = instrSpl[0]
b = instrSpl[1]
c = instrSpl[2]

if a < b & b < c:
    print("Yes")
else:
    print("No")

