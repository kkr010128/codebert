n = int(input())
suretsu = list(map(int,input().split()))

wa = 0
minimum = suretsu[0]
maximum = suretsu[0]

for i in range(n):
    wa += suretsu[i]
    if suretsu[i] > maximum:
        maximum = suretsu[i]
    if suretsu[i] < minimum:
        minimum = suretsu[i]
    
print (minimum,maximum,wa)