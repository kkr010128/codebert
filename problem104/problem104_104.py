l,r,d = [int(x) for x in input().split(' ')]
st = (l+d-1)//d
en = r//d
print(en-st+1)