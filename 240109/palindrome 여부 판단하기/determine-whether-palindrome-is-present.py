A = input()
l = 0
r = len(A)
def is_palindrome(A):
    for i in range(l // 2+1):
        if A[i] != A[r-i-1]:
            return False
    return True
if is_palindrome(A):
    print("Yes")
else:
    print("No")