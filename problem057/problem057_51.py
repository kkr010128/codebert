JUDGE_LIST=[[80, "A"],
            [65, "B"],
            [50, "C"],
            [30, "D"]]

while True:
    try:
        score=[int(x) for x in raw_input().split(" ")]
    except EOFError:
        break
    
    if score[0]==-1 and score[1]==-1 and score[2]==-1:
        break
    
    if score[0]==-1 or score[1]==-1:
        print "F"
        continue

    for judge in JUDGE_LIST:
        if judge[0] <= score[0] + score[1]:
            if "D" == judge[1] and score[2] >= 50:
                print "C"
                break
            else:
                print judge[1]
                break
    else:
        print "F"