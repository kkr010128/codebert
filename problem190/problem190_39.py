S=input()
T=True
for i in range(int((len(S)-1)/2)-1):
  if S[i]!=S[int(len(S))-1-i]:
    T=False
for i in range(int((len(S)-3)/4)+1):
  if S[i]!=S[int((len(S)-3)/2)-i]:
    T=False
if T==False:
  print("No")
else:
  print("Yes")