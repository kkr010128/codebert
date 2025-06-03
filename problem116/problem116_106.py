word_1 = [i for i in map(str,input())]
count =0
word_2 = [i for i in map(str,input())]
for key,item in enumerate(word_1):
    if not item == word_2[key]:
      count += 1
print(count)