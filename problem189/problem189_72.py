#A
n,m=map(int,input().split())
if n<=1:
    n_ans=0
else:
    n_ans=n*(n-1)/2

if m<=1:
    m_ans=0
else:
    m_ans=m*(m-1)/2
    

print(int(n_ans+m_ans))