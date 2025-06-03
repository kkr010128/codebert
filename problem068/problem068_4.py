def sprint(str, a, b):
 print(str[a:b+1])

def reverse(str, a, b):
 str1 = str[:a]
 str2 = str[a: b+1]
 str3 = str[b+1:]
 str = str1 + str2[::-1] + str3
 return str

def replace(str, a, b, p):
 str1 = str[:a]
 str3 = str[b+1:]
 str = str1 + p + str3
 return str

str = input()
q = int(input())
for i in range(q):
 L = input().split()
 if L[0] == "replace":
  str = replace(str, int(L[1]), int(L[2]), L[3])
 if L[0] == "reverse":
  str = reverse(str, int(L[1]), int(L[2]))
 if L[0] == "print":
  sprint(str, int(L[1]), int(L[2]))