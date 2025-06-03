n = int(input())
an = [int(num) for num in input().split()]

sum = 0
for i in range(len(an)-1):
  if an[i] > an[i+1]:
    sum += an[i] - an[i+1]
    an[i+1] += an[i] - an[i+1]
    
print(sum)