k=int(input())
se=0
for i in range(k):
    se=se*10
    se+=7
    i+=1
    if se%k==0:
        print(i)
        exit()
    se%=k
print('-1')