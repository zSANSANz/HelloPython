def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if (a[i] > b[i]):
            alice = alice + 1
        
        if (a[i] < b[i]):
            bob = bob + 1 
        
    return [alice, bob]


# Test case
a = [5, 2, 3]
b = [1, 4, 6]
result = compareTriplets(a, b)
print(result)  #Output: [2, 1]