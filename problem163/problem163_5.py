sheep_str,wolf_str= input().split()
sheep = float(sheep_str)
wolf = float(wolf_str)

if sheep <= wolf:
  print("unsafe")
else:
  print("safe")