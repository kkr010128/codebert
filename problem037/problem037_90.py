s = int(input())
sec = s%60
min = s//60 # may be more than 60
hr = min//60
min = min%60

print(hr, min, sec, sep=':')
