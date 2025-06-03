import sys

def main():
  for line in sys.stdin:
    print(int(line.strip())**3)

if __name__ == "__main__":
  main()