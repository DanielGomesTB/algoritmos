import statistics
def median(arr):
    # Write your code here
    arr.sort()
    return statistics.median(arr)
    
print(median([5, 3, 1, 2, 4]))