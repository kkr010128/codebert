N = int(input())
taro_p = hana_p = 0
for n in range(N):
  tw,hw = input().split()
  if tw == hw:
    taro_p += 1
    hana_p += 1
  elif tw < hw:
    hana_p += 3
  else :
    taro_p += 3

print(taro_p,hana_p)