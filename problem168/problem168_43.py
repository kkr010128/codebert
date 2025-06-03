N, M = map(int, input().split())
task = []
for i in range(1, M + 1):
    task.append("A_" + str(i))

task = map(int, input().split())
task_total = sum(task)

if task_total <= N:
    print(N - task_total)

else:
    print(-1)
