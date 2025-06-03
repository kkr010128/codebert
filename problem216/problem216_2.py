# -*- coding: utf-8 -*-
ABC = input()
ABC = ABC.replace(" ", "")
if ABC.count(ABC[0]) == 2 or ABC.count(ABC[1]) == 2 or ABC.count(ABC[2]) == 2:
  print("Yes")
else:
  print("No")