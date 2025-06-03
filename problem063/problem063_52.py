s=''
try:
  while True:
   sentence=input()
   s+=sentence.lower()
except:
    for i in[chr(i) for i in range(97,97+26)]:
     print(i,':',s.count(i))