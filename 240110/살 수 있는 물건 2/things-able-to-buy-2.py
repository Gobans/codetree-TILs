n = int(input())
if n >=3000:
    answer = "book"
elif n >= 1000:
    answer = "mask"
elif n>= 500:
    answer = "pen"
else:
    answer = "no"
print(answer)