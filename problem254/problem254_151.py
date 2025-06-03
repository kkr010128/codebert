A = int(input())
B = int(input())

answer = [1,2,3]
answer = set(answer)
wrong = set([A, B])

temp = answer - wrong 
print(temp.pop())