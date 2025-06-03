import sys
input = sys.stdin.readline
H,W,K =list(map(int,input().split()))
s = [input().rstrip() for _ in range(H)]
cut = [[0]*W for _ in range(H)]
cnt =0
for ih in range(H):
    if s[ih].count('#')==0:
        continue
    else:
        for iw in range(W):
            if s[ih][iw] == '#':
                cnt +=1
                cut[ih][iw]= cnt

for ih in range(H):
    for iw in range(W-1):
        if cut[ih][iw+1] ==0:
            cut[ih][iw+1]= cut[ih][iw]
    for iw in range(W-1,0,-1):
        if cut[ih][iw-1] ==0:
            cut[ih][iw-1]= cut[ih][iw]
        
for ih in range(H-1):
    if cut[ih+1][0]==0:
        for iw in range(W):
            cut[ih+1][iw] = cut[ih][iw]
for ih in range(H-1,0,-1):
    if cut[ih-1][0]==0:
        for iw in range(W):
            cut[ih-1][iw] = cut[ih][iw]
for i in range(H):
    print(*cut[i])
