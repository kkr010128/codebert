H,A = map(int,input().split())
div,mod = divmod(H,A)
print(div if mod==0 else div+1)