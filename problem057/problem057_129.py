while True:
    mid_score, term_score, re_score = map(int, input().split())
    if mid_score == term_score == re_score == -1:
        break
    test_score = mid_score + term_score
    score = ''
    if test_score >= 80:
        score = 'A'
    elif test_score >= 65:
        score = 'B'
    elif test_score >= 50:
        score = 'C'
    elif test_score >=30:
        if re_score >= 50:
            score = 'C'
        else:
            score = 'D'
    else:
        score = 'F'
    if mid_score == -1 or term_score == -1:
        score = 'F'
    print(score)

