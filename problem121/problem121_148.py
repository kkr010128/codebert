alpha = [chr(i + 97) for i in range(26)] 
N = int(input())
name = ''
while N >= 1:
  N -= 1
  _ = N % 26
  name += alpha[_]
  N //= 26
  
print(name[-1::-1])