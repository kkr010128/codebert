p=input()
s=input()

ret = 'Yes'
try: (p+p).index(s)
except : ret = 'No'
print(ret)