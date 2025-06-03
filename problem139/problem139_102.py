h,m,H,M,K=map(int,input().split())

pre=60*h+m
post=60*H+M

print(post-pre-K)