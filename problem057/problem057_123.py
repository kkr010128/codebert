out_grade = ""

while True:
    m, f, r = map(int, input().split(" "))

    if m==f==r==-1:
        #EOF
        break
    
    if m==-1 or f==-1:
        out_grade = "F"
    elif m + f >= 80:
        out_grade = "A"
    elif m + f >= 65:
        out_grade = "B"
    elif m + f >= 50:
        out_grade = "C"
    elif m + f >= 30:
        if r >= 50:
            out_grade = "C"
        else:
            out_grade = "D"
    else:
        out_grade = "F"
    
    print(out_grade)