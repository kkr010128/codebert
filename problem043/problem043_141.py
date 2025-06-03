def get_input():
  lst = []
  pair = [int(n) for n in input().split(" ")]
  while pair != [0, 0]:
    lst.append(pair)
    pair = [int(n) for n in input().split(" ")]
  return lst

def to_str(lst):
  return [str(n) for n in lst]

lst = get_input()
for pair in lst:
  print(' '.join(to_str(sorted(pair))))