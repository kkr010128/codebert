S = input()
N = len(S)
count1,count2,count3 = 0,0,0
flg1,flg2,flg3 = False,False,False
for i in range(N):
    #print(S[i],S[-1-i])
    if S[i] == S[-1-i]:
        count1 += 1
if count1 == N:
    flg1 = True
#print(count1,flg1)
a = int((N-1)/2)
for i in range(a):
    #print(S[i],S[a-1-i])
    if S[i] == S[a-1-i]:
        count2 += 1
if count2 == int((N-1)/2):
    flg2 = True
#print(count2,flg2,a)
b = int((N+3)/2)
#print(b)
for i in range(N-b+1):
    #print(S[b+i-1],S[N-1-i])
    if S[b+i-1] == S[N-i-1]:
        count3 += 1
if count3 == N-b+1 :
    flg3 = True
if flg1 == True and flg2 == True and flg3 == True:
    print("Yes")
else:
    print("No")
