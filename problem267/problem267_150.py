n = int(input())
numbers = input()

lst = set()
ans = []
for i in range(n):
  pin = ''
  if numbers[i] not in lst:
    pin += numbers[i]
    lst.add(pin)
    lst2 = set()
    for j in range(i+1, n):
      pin += numbers[j]
      if pin[1] not in lst2:
        lst2.add(pin[1])
        lst3 = set()
        for k in range(j+1, n):
          pin += numbers[k]
          if pin[2] not in lst3:
            lst3.add(pin[2])
            ans.append(pin)
          if ('0' in lst3) and ('1' in lst3) and ('2' in lst3) and ('3' in lst3) and ('4' in lst3) and ('5' in lst3) and ('6' in lst3) and ('7' in lst3) and ('8' in lst3) and ('9' in lst3):
            break
          pin = pin[0] + pin[1]
      if ('0' in lst2) and ('1' in lst2) and ('2' in lst2) and ('3' in lst2) and ('4' in lst2) and ('5' in lst2) and ('6' in lst2) and ('7' in lst2) and ('8' in lst2) and ('9' in lst2):
        break
      pin = pin[0]
    if ('0' in lst) and ('1' in lst) and ('2' in lst) and ('3' in lst) and ('4' in lst) and ('5' in lst) and ('6' in lst) and ('7' in lst) and ('8' in lst) and ('9' in lst):
      break
print(len(ans))
