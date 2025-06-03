S = input()
T = input()

time = []

S_list = list(S)
T_list = list(T)

Len = (len(S))
listt = list(range(Len))

for ss in listt:
      if S[ss] ==T[ss]:
            None
      else:
            time.append(ss)

print(len(time))




