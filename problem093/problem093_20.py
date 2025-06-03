N, K = map(int, input().split())
p_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_score = 0
first = True
for i in range(N):
  score = 0
  step = 0
  path = {}
  cumulative_score = []
  current_p = i
  cycle_passed = False
  while step < K:
    # record current step
    cumulative_score.append(score)
    
    # check if cycle is found
    if (not cycle_passed) and (current_p in path.keys()):
      # found a cycle 
      # calculate score sum within the cycle
      # calculate steps with in the cycle
      cycle_start_step = path[current_p]
      cycle_steps = step - cycle_start_step
      cycle_sum = cumulative_score[step] - cumulative_score[cycle_start_step]
      if cycle_sum < 0:
        # negative cycle
        # finish 
        break
      else:
        #positive cycle
        remain_steps = K - step
        if remain_steps > cycle_steps:
          cycle_times = (K - step) // cycle_steps - 1
          step += (cycle_times * cycle_steps)
          score += (cycle_times * cycle_sum)
          cycle_passed = True
        else:
          cycle_passed = True    
        
    # record current step
    path[current_p] = step
    
    # go to next step
    next_p = p_list[current_p-1]
    score += c_list[next_p-1]
    if (first):
      max_score = score
      first = False
    else:
      max_score = max(max_score, score)
    
    current_p = next_p
    step += 1

print(max_score)