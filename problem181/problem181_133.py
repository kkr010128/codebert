k = int(input())

queue = [1,2,3,4,5,6,7,8,9]
cnt = 0
while cnt + len(queue) < k:
  cnt += 1
  n = queue.pop(0)
  if n%10 != 0:
    queue.append(n*10+n%10-1)
  queue.append(n*10+n%10)
  if n%10 != 9:
    queue.append(n*10+n%10+1)
print(queue[k-cnt-1])