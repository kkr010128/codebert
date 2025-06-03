D=int(input())
C=list(map(int, input().split()))
S=[list(map(int,input().split())) for i in range(D)]

T=[]
for i in range(D):
  T.append(int(input()))

def dissat(day):
  dissat = 0
  for i in range(26):
    if T[day-1]-1 == i:
      continue
    dissat += C[i]*(day-lastdays[i])

  return dissat    
    
def last(day):
  lastdays[T[day-1]-1] = day

sat = 0
lastdays = [0]*26

# main
for i in range(D):
  # dayi
  last(i)
  sat += S[i][T[i]-1] - dissat(i+1)
  print(sat)
