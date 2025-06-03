S = input()
print("Yes" if ( S==S[::-1] and S[:int((len(S)-1)/2)]==S[:int((len(S)-1)/2)][::-1] ) else "No")
