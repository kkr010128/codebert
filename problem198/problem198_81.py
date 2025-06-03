n = int(input())
 
def aa(str, chrMax):
  if len(str) == n:
    print(str)
    return
  for i in range(ord("a"), ord(chrMax)+2):
    if i > ord(chrMax):
      aa(str+chr(i), chr(i))
    else:
      aa(str+chr(i), chrMax)
 
aa("a", "a")