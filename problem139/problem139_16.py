h1,m1,h2,m2,k=map(int,raw_input().split())

print max(h2*60+m2-h1*60-m1-k,0)