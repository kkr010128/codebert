AL=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
N=input()
l=0
for i in AL:
  if N==i:
    print(AL[l+1])
  else:
    l+=1