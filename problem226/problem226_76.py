H,N= map(int, input().split())
list = list(map(int, input().split())) #Aiを入力


for i in list:
    H=H-i

if H<=0:
    print('Yes')
else:
    print('No')
