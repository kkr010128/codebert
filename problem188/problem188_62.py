x,y,a,b,c = map(int,input().split()) 

R=list(map(int,input().split()) )
G=list(map(int,input().split()) )
W=list(map(int,input().split()) )

R.sort(reverse=True)
G.sort(reverse=True)

Z = W+R[0:x] + G[0:y]

Z.sort(reverse=True)

print(sum(Z[0:x+y]))

