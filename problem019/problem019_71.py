from collections import deque;

count, time_slice = map(int, input().split(" "));

data = [];
for i in range(count):
    data += input().split(" ");

def round_robin(data, count, time_slice):
    t = 0;
    data = [[data[i], int(data[i + 1])] for i in range(0, len(data), 2)];
    que = deque(data);
    while len(que) > 0:
        current = que.popleft();
        if current[1] > time_slice:
            current[1] -= time_slice;
            t += time_slice;
            que.append(current);
        else:
            t += current[1];
            print(current[0], t);


round_robin(data, count, time_slice);
