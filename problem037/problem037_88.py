S=input()
h=int(S)/3600
m=(int(S)%3600)/60
s=((int(S)%3600)%60)/1
print(int(h),':',int(m),':',int(s),sep='')
