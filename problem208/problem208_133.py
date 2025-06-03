n,m = map(int, input().split())

s=[]
for i in range(m):
    s.append(list(map(int, input().split())))
if n==1:
    kaisuu_start=0
    kaisuu_stop=10
elif n==2:
    kaisuu_start=10
    kaisuu_stop=100
elif n==3:
    kaisuu_start=100
    kaisuu_stop=1000
    
for suuzi in range(kaisuu_start,kaisuu_stop):
    hantei=True
    suuzi=str(suuzi)
    for gyou in range(m):
        if suuzi[s[gyou][0]-1]!=str(s[gyou][1]):
            hantei=False
            continue
    if hantei:
        print(suuzi)
        exit()

print(-1)