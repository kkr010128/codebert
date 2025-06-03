S = input()
K = int(input())
 
INNER = 0
  
if len(set(list(S))) == 1:
  print(K*len(S)//2)
else: 
  i = 0
  while i < len(S)-1:
    if S[i] == S[i+1]:
      INNER += 1
      i += 1
    i += 1
  
  if (S[0] != S[-1]):#最初の文字と最後の文字が違うなら、
    print(INNER*K)
  else:
    same_from_start = 0
    same_from_end = 0
    
    count_from_start = 0
    count_from_end = 0
    
    flag_same_from_start = 0
    flag_same_from_end = 0
    
    while flag_same_from_start == 0:
      if S[count_from_start] == S[count_from_start+1]:
        count_from_start += 1
      else:
        count_from_start += 1
        flag_same_from_start = 1
    
    while flag_same_from_end == 0:
      if S[len(S)-count_from_end-1] == S[len(S)-count_from_end-2]:
        count_from_end += 1
      else:
        count_from_end += 1
        flag_same_from_end = 1
    print(INNER*K + (K -1) * ((count_from_start+count_from_end)//2 -\
                              count_from_start//2- count_from_end//2))