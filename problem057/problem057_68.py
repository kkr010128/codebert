scores = []
while True:
    score = list(map(int, input().split()))
    if score[0] == -1 and score[1] == -1 and score[2] == -1:
        break
    else:
        scores.append(score)

for i in scores:
    mid_exam = i[0]
    final_exam = i[1]
    re_exam = i[2]
    total = i[0] + i[1]
    if mid_exam == -1 or final_exam == -1:
        print("F")
    elif total >= 80:
        print("A")
    elif total in range(65, 80):
        print("B")
    elif total in range(50, 65):
        print("C")
    elif 30 <= total < 50:
        if re_exam >= 50:
            print("C")
        else:
            print("D")
    elif total < 30:
        print("F")