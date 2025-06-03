while True:
    score = [int(i) for i in input().split()]
    if score == [-1, -1, -1]:
        break
    sum = score[0] + score[1]
    if sum < 30 or score[0] == -1 or score[1] == -1:
        print('F')
    elif sum < 50 and score[2] < 50:
        print('D')
    elif sum < 65 or (sum < 65 and score[2] >= 50):
        print('C')
    elif sum < 80:
        print('B')
    elif sum >= 80:
        print('A')

