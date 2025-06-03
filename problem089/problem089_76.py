R, C, T = map(int, input().split())
RC = []
for _ in range(T):
    RC.append(list(map(int, input().split())))
TR = [0] * (R + 1)
TC = [0] * (C + 1)
mxr=0
mxc=0
for r, c in RC:
    TR[r] += 1
    TC[c] += 1
    if(TR[r]>mxr):
      mxr=TR[r]
    if(TC[c]>mxc):
      mxc=TC[c]
ct = TR.count(mxr) * TC.count(mxc) - len([0 for r, c in RC if TR[r] == mxr and TC[c] == mxc])
print(mxc + mxr - (ct == 0))