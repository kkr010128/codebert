from queue import Queue

k = int(input())
q = Queue()
for i in range(1, 10):
    q.put(i)
for i in range(k):
    x = q.get()
    if x % 10 != 0:
        num = 10 * x + (x % 10) - 1
        q.put(num)
    num = 10 * x + (x % 10)
    q.put(num)
    if x % 10 != 9:
        num = 10 * x + (x % 10) + 1
        q.put(num)
print(x)