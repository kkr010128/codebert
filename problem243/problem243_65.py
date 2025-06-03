N = int(input())
s_list = []
t_list = []
for i in range(N):
    s,t=input().split()
    s_list.append(s)
    t_list.append(int(t))
    
X = input()

flag = 0
time = 0

for i, x in enumerate(s_list):
  if x == X:
    flag = 1
  
  elif flag == 1:
    time += t_list[i]
print(time)