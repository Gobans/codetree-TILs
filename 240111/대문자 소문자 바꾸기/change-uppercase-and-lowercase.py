s = input()
answer = ""
lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
for c in s:
    if c in lower_alphabets:
        answer += c.upper()
    else:
        answer += c.lower()
print(answer)