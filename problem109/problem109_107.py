N=int(input())
ac = wa = tle = re =0
for cnt in range(N):
  S=input()
  if S=='AC':
    ac=ac+1
  elif S=='WA':
    wa=wa+1
  elif S=='TLE':
    tle=tle+1
  elif S=='RE':
    re=re+1
print('AC x '+str(ac)+'\nWA x '+str(wa)+'\nTLE x '+str(tle)+'\nRE x '+str(re))