s=int(input())

sec=s%60
min=s//60 #may be more than 60
hr=min//60
min=min%60

# line 3-6 can be replace with 9-11
hr=s//3600
min=(s//60)%60
sec=s%60

print(hr, min, sec, sep=':')
