i=input;i();x=1;l=i().split()
if '0' in l:
  print(0)
  quit()
for j in l:
  x*=int(j)
  if x > 1e18:
    print(-1);quit()
print(x)
