num =raw_input()
num = int(num)
h = num/3600
m = (num-h*3600)/60
s = num-h*3600-m*60
h,m,s = map(str,(h,m,s))
print h+':'+m+':'+s 