n=input()
h=n/3600
m=(n-h*3600)/60
print ':'.join(map(str,[h,m,n%60]))