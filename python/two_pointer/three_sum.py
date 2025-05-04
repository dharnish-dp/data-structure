'''
Given an array A, find all unique triplets in the array whose sum is equal to zero.

Example:
A: [1, 1, 0, -1, -2]
Triplets: [
  [-2, 1, 1],
  [-1, 0, 1]
]

'''

def threeSum(A):
    A.sort()  # Sort the array first
    length = len(A)
    result = []

    for i in range(length - 2):  # We need at least three elements
        if i > 0 and A[i] == A[i - 1]:  # Skip duplicate first elements
            continue

        j, k = i + 1, length - 1  # Two-pointer technique

        while j < k:
            total = A[i] + A[j] + A[k]
            if total == 0:
                result.append([A[i], A[j], A[k]])
                j += 1
                k -= 1
                # Skip duplicate second and third elements
                while j < k and A[j] == A[j - 1]:
                    j += 1
                while j < k and A[k] == A[k + 1]:
                    k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1

    return result

print(threeSum([1, 1, 0, -1, -2]))