
def diagonalDifference(arr):
    # Write your code here
    difference = 0
    primaryDiagonal = 0
    secondaryDiagonal = 0
    
    for i in range(len(arr)):
           primaryDiagonal = primaryDiagonal + arr[i][i]
           secondaryDiagonal += arr[i][len(arr) - 1 - i]
           print(primaryDiagonal, secondaryDiagonal)
    

    return abs(primaryDiagonal - secondaryDiagonal)


# Example test case
matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDifference(matrix)) # Output: 0