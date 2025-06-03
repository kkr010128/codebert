D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for _ in range(D)]
t=[int(input()) for _ in range(D)]

points=0
day_last=[0]*26

def minus(day):
    return sum([c[i]*(day+1-day_last[i]) for i in range(26)])

def plus(day,contest_number):
    return s[day][contest_number-1]

for day,contest_number in enumerate(t):
    day_last[contest_number-1]=day+1
    points=points+plus(day,contest_number)-minus(day)
    print(points)