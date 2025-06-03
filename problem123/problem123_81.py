N = int(input())
a = list(map(int,input().split()))
#xor_a = [bin(x) for x in a]
#print(xor_a)
x = 0
for i in a:
    x ^= i
b = [x^y for y in a]
print(' '.join(map(str, b))) #' 'joinにより空白を間にいれる。mapにより文字列に直す
#atcoderではforを使った普通の縦の並びでもいいらしい