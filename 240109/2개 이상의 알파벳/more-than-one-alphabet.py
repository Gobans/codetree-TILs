A = input()
def is_more_c(A):
    for i in range(len(A)-1):
        if A[i] in A[i+1:]:
            return True
    return False
if is_more_c(A):
    print("Yes")
else:
    print("No")