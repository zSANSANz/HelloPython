def aVeryBigSum(ar):
    # Write your code here
    bigSum = 0
    
    for i in range(len(ar)):
        bigSum = bigSum + ar[i]
    
    return bigSum


# Example usage
array = [1, 2, 3, 4, 10, 11]
arrayBig = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

result = aVeryBigSum(array)
print(result)  # Output: 31


resultBig = aVeryBigSum(arrayBig)
print(resultBig) # Output: 