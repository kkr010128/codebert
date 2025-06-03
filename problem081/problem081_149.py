dts_s = input().split()
dts_i = [int(n) for n in dts_s]
if dts_i[0]/dts_i[1] > dts_i[2]:
  print("No")
else:
  print("Yes")