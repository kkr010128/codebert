T = input()
T_list = list(T)
i = 0
for s in T_list:
  if i == len(T_list):
    break
  if i == 0:
    if T_list[i] == "?":
      if 1 < len(T_list):
        if T_list[i+1] == "D":
          T_list[i] = "P"
        elif T_list[i+1] == "?":
          T_list[i] = "P"
          T_list[i+1] = "D"
          i = i + 2
          continue
        else:
          T_list[i] = "D"
      else:
        T_list[i] = "D"
  else:
    if T_list[i] == "?":
      if T_list[i-1] == "P":
        T_list[i] = "D"
      elif i+1 < len(T_list):
        if T_list[i+1] == "D":
          T_list[i] = "P"
        elif T_list[i+1] == "?":
          T_list[i] = "P"
          T_list[i+1] = "D"
          i = i + 2
          continue
        else:
          T_list[i] = "D"
      else:
        T_list[i] = "D"
  i = i + 1
T = "".join(T_list)
print(T)