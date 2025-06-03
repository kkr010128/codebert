S=int(input())
a=S%60
b=(S//60)%60
c=S//3600
print("{0}:{1}:{2}".format(c,b,a))