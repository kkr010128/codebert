s = input()

s_list = list(s)

if s_list[-1] == 's':
  output = s + 'es'
else:
  output = s + 's'
  
print(output)