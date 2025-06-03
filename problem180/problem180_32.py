score = list(map(int,input().split()))

amari = score[0] % score[1]
kouho = score[1] - amari

if amari < kouho:
    print(amari)
else:
    print(kouho)