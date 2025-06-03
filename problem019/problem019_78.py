if __name__ == "__main__":
      S = (input()).split()
      n = int(S[0])
      q = int(S[1])
      head = 0
      tail = n-1
      que = []
      runtime = 0
      fin = []

      for i in range(0, n):
            que.append((input()).split())

      while head <= tail:
            nowjob = que[head]
            jobtime = int(nowjob[1])
            if jobtime > q :
                  jobtime = jobtime -q
                  jobname = nowjob[0]
                  que.append([jobname, jobtime])
                  runtime = runtime + q
                  head = head + 1
                  tail = tail + 1
            else :
                  runtime = runtime + jobtime
                  fin.append([(que[head])[0], runtime])
                  head = head + 1
      for i in range(0,n):
            print("{} {}".format((fin[i])[0], (fin[i])[1]))