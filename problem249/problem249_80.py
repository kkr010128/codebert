A,B,K = map(int,input().split())
if A>=K:
    answer = A-K,B
elif A+B>=K:
    answer = 0,B-(K-A)
else:
    answer = 0,0
print(answer[0],answer[1])