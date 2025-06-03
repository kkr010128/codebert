s=input()

w=['SUN','MON','TUE','WED','THU','FRI','SAT',]
w=w[::-1]

for i in range(7):
    if w[i]==s:
        print(i+1)
        break
    
