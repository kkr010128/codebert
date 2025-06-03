N = int(input())
cnt = [0]*4
judge = ["AC","WA","TLE","RE"]
for i in range(N):
    s = input()
    if s=="AC":
        cnt[0]+=1
    elif s=="WA":
        cnt[1]+=1
    elif s=="TLE":
        cnt[2]+=1
    else:
        cnt[3]+=1
for i in range(4):
    print(judge[i],"x",cnt[i])