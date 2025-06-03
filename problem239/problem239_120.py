import string
c = input()
abc_list = list(string.ascii_lowercase)
for num,string in enumerate(abc_list):
  if string == c:
    print(abc_list[num+1])