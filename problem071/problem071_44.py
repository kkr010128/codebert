str = input() # sを取得し、strに値を入れる
if str[len(str)-1] == 's':
  #str = str[:len(str)-1]
  print(str + 'es')
else:
  print(str + 's')
