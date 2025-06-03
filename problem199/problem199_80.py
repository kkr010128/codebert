s = input()

result = 'No'

if len(s) % 2 == 0:
   result = 'Yes'
   for i in range(int(len(s) / 2)):
      if s[i*2:i*2+2] != 'hi':
         result = 'No'
         break

print(result)