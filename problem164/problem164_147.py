ha,sa,hb,sb = list(map(int, input().split()))
while ha>0 and hb>0:
  hb -= sa
  if hb<=0: break
  ha -= sb
print('Yes' if ha>0 else 'No')