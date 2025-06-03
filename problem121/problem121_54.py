N = int(input())
def numalpha(num):
  if num <= 26:
    return chr(64+num)
  elif num % 26 == 0:
    return numalpha(num//26-1)+chr(90)
  else:
    return numalpha(num//26)+chr(64+num%26)
print(numalpha(N).lower())