T = input()
lt = list(T)
for i in range(len(lt)):
  if lt[i] == '?':
    lt[i] = 'D'
T = ''.join(lt)
print(T)