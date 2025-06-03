import sys
import numpy as np

def main():
  input = sys.stdin.readline
  d = int(input())
  c = np.array([int(x) for x in input().split()])
  
  last = np.zeros(26, dtype="int64")
  
  for i in range(d):
    s = np.array([int(x) for x in input().split()])
    key, value = -1, -1
    for i in range(26):
      if value < s[i] + last[i]:
        key = i
        value = s[i] + last[i]
    last[key] = 0
    print(key+1)
    last += c

if __name__ == "__main__":
  main()