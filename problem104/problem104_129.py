l, r, d = map(int, input().split())

rest = l%d

if(rest == 0):
	num = int(r/d) - int(l/d) + 1
else:
  	num = int(r/d) - int(l/d)
    
print(num)