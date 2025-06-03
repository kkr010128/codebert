#template
def inputlist(): return [int(j) for j in input().split()]
#template
a,b,c,d = inputlist()
print(max(a*c,a*d,b*c,b*d))