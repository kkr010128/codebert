import queue

n = int(input())
alp = "abcdefghijklmn"
q = queue.Queue()
q.put("a")
while not q.empty():
    qi = q.get()
    if len(qi) == n:
        print(qi)
    elif len(qi) < n:
        idx = alp.index(max(qi))
        for i in range(idx+2):
            q.put(qi+alp[i])
