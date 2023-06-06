def simpleArraySum(ar):
    # Write your code here
    hasil = 0
    for i in range(len(ar)): 
        hasil = hasil + ar[i]
    return hasil

# Example usage
array = [1, 2, 3, 4, 10, 11]
result = simpleArraySum(array)
print(result)  # Output: 31