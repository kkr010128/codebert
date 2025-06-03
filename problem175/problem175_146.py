N = int(input())
S = input()
count_R = 0
count_G = 0
count_B = 0
count = 0
for i in range(N):
    if S[i] == 'R':
        count_R = count_R+1
    elif S[i] == 'G':
        count_G = count_G+1
    else:
        count_B = count_B+1
count = count_R*count_G*count_B

for i in range(N):
  for j in range(i+1,N):
    if S[i] != S[j]:
      k = 2*j-i
      if k>=N:
        break
      else:
        if S[i] != S[k] and S[j] != S[k]:
          count = count-1
print(count)