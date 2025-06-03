S=input()

Week=['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(7):
  if S==Week[i]:
    today=i
    
print(7-today)