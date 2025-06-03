S = input()

S_list = list(S)
N = len(S_list)
#print(N)
no_flag = 0

for i in range(N//2):
    if S_list[i] != S_list[N-i-1]:
        no_flag = 1

for i in range(int((N-1)/2)//2):
    #print(S_list[i], S_list[(N-1)//2-i-1])
    if S_list[i] != S_list[(N-1)//2-i-1]:
        no_flag = 1

for i in range((N-3)//2):
    #print(S_list[(N+3)//2+i-1], S_list[N-1-i])
    if S_list[(N+3)//2+i-1] != S_list[N-1-i]:
        no_flag = 1

if no_flag == 1:
    print("No")
else:
    print("Yes")
