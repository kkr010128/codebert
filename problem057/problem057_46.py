student_info = []
while True:
    s = map(int,raw_input().split(" "))

    if s[0] is s[1] is s[2] is -1:
        break
    
    student_info.append(s)

score_info = []
for s in student_info:
    if s[0] == -1 or s[1] == -1:
        score_info.append("F")

    elif s[0]+s[1] >= 80:
        score_info.append("A")

    elif 65 <= s[0]+s[1] < 80:
        score_info.append("B")

    elif 50 <= s[0]+s[1] < 65:
        score_info.append("C")

    elif 30<= s[0]+s[1] < 50:
        if s[2] >= 50:
            score_info.append("C")
        else:
            score_info.append("D")
    else:
        score_info.append("F")

for i in score_info:
    print i