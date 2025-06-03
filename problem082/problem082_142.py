S = list(str(input()))
T = list(str(input()))
s = 0
t = 0
len_s = len(S)
len_t = len(T)
i = 0
ans = []

while i < len_s-len_t+1:
    cnt = 0
    #print(S[i:i+len_t])
    for ss, tt in zip(S[i:i+len_t], T):
        #print(ss,tt)
        if ss != tt:
            cnt +=1
    ans.append(cnt)
    i += 1

#print(ans)
print(min(ans))