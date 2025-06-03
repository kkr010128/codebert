c = input()
alpha_list = 'abcdefghijkfmnopqrstuvrxyz'

for i in range(len(alpha_list)):
  if c == alpha_list[i]:
    print(alpha_list[i+1])
    break