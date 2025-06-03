n = int(input())
s, t = input().split()
 
answer_list = []
for i in range(n):
  answer_list.append(s[i])
  answer_list.append(t[i])

joint = ''.join(answer_list)
print(joint)