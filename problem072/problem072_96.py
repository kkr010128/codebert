counter = int(input())
result_flg = False

fir_fir, fir_sec = map(int, input().split())
sec_fir, sec_sec = map(int, input().split())


for i in range(2, counter):
  thi_fir, thi_sec = map(int, input().split())

  if fir_fir == fir_sec:
    if sec_fir == sec_sec:
      if thi_fir == thi_sec:
        result_flg = True
        break

  # reset content
  fir_fir = sec_fir
  fir_sec = sec_sec
  sec_fir = thi_fir
  sec_sec = thi_sec

if result_flg == True:
  print('Yes')
else:
  print('No')