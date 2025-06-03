a,b,c,d = map(int,input().split())

answers = []

one = a*c
two = a*d
three = b*c
four = b*d

answers.append(one)
answers.append(two)
answers.append(three)
answers.append(four)

print(max(answers))