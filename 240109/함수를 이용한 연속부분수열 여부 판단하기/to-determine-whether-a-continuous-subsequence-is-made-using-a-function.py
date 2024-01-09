n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def find_partitial_array(A, B):
    n1 = len(A)
    n2 = len(B)
    for i in range(n1-n2+1):
        if A[i:i+n2] == B:
            return True
    return False
if find_partitial_array(A, B):
    print("Yes")
else:
    print("No")