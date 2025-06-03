n=int(input())
dept=100000
for i in range(n):
    dept*=1.05
    if dept%1000!=0:
        dept=dept-dept%1000+1000
print(int(dept))