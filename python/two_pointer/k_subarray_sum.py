'''
K-Subarray Sum
Given an array and a number k, find the sum of all the subarrays of size k.

Example
Array: [3, 5, 6, 2, 4, 7, 8]
k: 3
Here, the subarrays of size k and their sum are:
[3 5 6] => 14
[5 6 2] => 13
[6 2 4] => 12
[2 4 7] => 13
[4 7 8] => 19
Answer: [14, 13, 12, 13, 19]

'''

def kSubarraySum(A):
    length = len(A)
    i = 0
    answer = []
    init = sum(A[i:k])
    answer.append(init)
    while i+k<length:
        init = init - A[i] + A[i+k]
        answer.append(init)
        i += 1
    return answer


A = [3, 5, 6, 2, 4, 7,8]
k = 3
print(kSubarraySum(A))  # Output: [14, 13, 12,13, 19]  # Correct output