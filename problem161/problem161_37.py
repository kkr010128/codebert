a,b,n = map(int,input().split())

i = min(b-1,n)
calc = (a*i)//b - (a * (i//b))

print(calc)
