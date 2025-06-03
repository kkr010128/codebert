N = int(input())
S = input()
count = 0

RGBlist = [[S.count('R')],[S.count('G')],[S.count('B')]]


for i in range(1,N):
    RGBlist[0].append(RGBlist[0][-1] - (S[i-1] == 'R'))
    RGBlist[1].append(RGBlist[1][-1] - (S[i-1] == 'G'))
    RGBlist[2].append(RGBlist[2][-1] - (S[i-1] == 'B'))

for i in range(N-2):
    si = S[i]
    
    for j in range(i+1,N-1):
        sj = S[j]
        if si==sj:
            continue
        else:
            RGB = set(['R','G','B'])
            RGB -= set([si,sj])
            k=j+1
            kji=j-i
            if RGB == {'R'}:
                rgb = 0
            elif RGB =={'G'}:
                rgb = 1
            else:
                rgb = 2
            if k+kji-1 < len(S):
                count += RGBlist[rgb][k] - ({S[k+kji-1]} == RGB)
            else:
                count += RGBlist[rgb][k]
            
print(count)
