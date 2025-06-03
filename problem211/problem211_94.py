a,b=map(int, input().split()) 

if a <= 9 :
    c = b + 100*(10-a)
else:
    c = b
print(c)