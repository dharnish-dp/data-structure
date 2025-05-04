'''
k-th symbol in Grammar
Coding Exercise (k-th symbol in Grammar)
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110. Given two integer n and k, 
return the kth (1-indexed) symbol in the nth row of a table of n rows.
'''

def kth_symbol(n, k):
    # Base case: first row only contains 0
    if n==1:
        return 0
    t = n**(n-1)
    mid = t//2
    if k<=mid:
        return kth_symbol(n-1,k)
    else:
        return 1-kth_symbol(n-1,k-mid)
    

# Test cases
print("Test Case 1:", kth_symbol(3, 2))  # Should return 1 (3rd row: 0110, 2nd position)
print("Test Case 2:", kth_symbol(1, 1))  # Should return 0 (1st row: 0, 1st position)
print("Test Case 3:", kth_symbol(2, 2))  # Should return 1 (2nd row: 01, 2nd position)
print("Test Case 4:", kth_symbol(4, 5))  # Should return 1 (4th row: 01101001, 5th position)
print("Test Case 5:", kth_symbol(3, 1))  # Should return 0 (3rd row: 0110, 1st position)