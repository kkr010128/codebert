n=int(input())
l=list(map(int,input().split()))

n_lis=[i for i in range(1,n+1)]
dic={i:j for i,j in zip(l,n_lis)}
num_lis=[str(dic[i]) for i in range(1,n+1)]
print(' '.join(num_lis))