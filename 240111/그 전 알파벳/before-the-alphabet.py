c = input()
if c == "a":
    print("z")
else:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = alphabet.index(c)
    previous_char = alphabet[index - 1]
    print(previous_char)