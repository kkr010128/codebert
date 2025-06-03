# -*- coding: utf-8 -*-

S = input()

ans = 'Yes'
for i in range(len(S)//2):
  if S[i] != S[len(S)-1-i]:
    ans = 'No'

front = S[0:(len(S)-1)//2]
for i in range(len(front)//2):
  if front[i] != front[len(front)-1-i]:
    ans = 'No'

end = S[(len(S)+1)//2:]
for i in range(len(end)//2):
  if end[i] != front[len(end)-1-i]:
    ans = 'No'
print(ans)