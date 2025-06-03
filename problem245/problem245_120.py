import sys
N = int( input() )
S = input()
count = 0
for i in range(len(S)):
    if S[i:i+3] =="ABC":
        count+=1
print(count)