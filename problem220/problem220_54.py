color = input()

kosuu = input()

trashc = input()

_ = 0

color = color.split()
kosuu = kosuu.split()
trashc = trashc.split()


while True:
  if(trashc[0] == color[_]):
    kosuu[_] = int(kosuu[_]) -1
    break
      
  _= _+1
    
print(" ".join(map(str, kosuu)))
