def min_swaps_to_sort(n, order):

    values = [ord(char) - ord('A') for char in order.split()]

    swaps = 0    

    for i in range(n):
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                swaps += 1
    
    return swaps

n = int(input())
order = str(input())
print(min_swaps_to_sort(n, order))