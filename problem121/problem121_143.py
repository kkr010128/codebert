n = int(input())
name_base = []
dog_name = ''
while n > 0:
  ch_mod = (n-1)%26
  n = (n-1)//26
  name_base.append(ch_mod)
for i in name_base:
  dog_name = dog_name + chr(i+97)
print(dog_name[::-1])