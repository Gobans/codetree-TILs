def is_palindrome(s):
    l = 0
    r = len(s)-1
    for _ in range(len(s) // 2):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y+1):
    if is_palindrome(str(i)):
        cnt += 1
print(cnt)