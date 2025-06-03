if __name__ == '__main__':
  s = str(input())

  if s[-1] != 's':
    print(f'{s}s')
  else:
    print(f'{s}es')