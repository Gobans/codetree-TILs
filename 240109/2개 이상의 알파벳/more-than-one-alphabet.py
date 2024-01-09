A = input()
def is_more_c(A):
    f = A[0]
    for i in range(1, len(A)):
        if A[i] != f:
            return True
    return False
if is_more_c(A):
    print("Yes")
else:
    print("No")