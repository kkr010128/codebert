n=input()
div=0
for ch in n:
    num=int(ch)
    div+=num

if div%9==0:
    print("Yes")
else:
    print('No')