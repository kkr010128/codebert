S=input()
result=7
l=['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in l:
    if i != S:
        result=result-1
    else:
        break
print(result)
