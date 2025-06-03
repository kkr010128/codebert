a_1, a_2, a_3 = map(int, input().split())
print('bust' if a_1+a_2+a_3 >= 22 else 'win')