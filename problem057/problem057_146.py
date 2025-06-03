m,f,r = map(int,input().split())
score = 0

while m!=-1 or f!=-1 or r!= -1:
    score = m+f
    if m==-1 or f ==-1:
        grade = "F"
    elif score >= 80:
        grade = "A"
    elif score < 80 and score >= 65:
        grade = "B"
    elif score < 65 and score >= 50:
        grade = "C"
    elif score < 50 and score >= 30:
        if r>=50:
            grade = "C"
        else:
            grade = "D"
    else:
        grade = "F"

    print(grade)
    m,f,r = map(int,input().split())