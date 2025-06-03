from sys import stdin

# read input
n,m = [int(x) for x in stdin.readline().strip().split()]
sc_dict = {}

# create dict
for _ in range(m):
  s, c = [int(x) for x in stdin.readline().strip().split()]
  if s in sc_dict.keys(): sc_dict[s].append(c)
  else: sc_dict[s] = [c]
    
# get min
min_val = list(str(10**(n-1))) if n > 1 else ['0']
for k, v in sc_dict.items():
  if len(v) != 1 and len(set(v)) > 1:
    print('-1')
    exit()
  min_val[k-1] = str(v[0])
  
min_val = ''.join(min_val)
if len(min_val) > 1 and int(min_val) == 0:
  print('-1')
else:
  print(''.join(min_val))