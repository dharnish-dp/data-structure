'''
Given a sorted array A, find the size of array A after removing the duplicate elements.

Examples:
A: [1 2 3 3 3 4 5 5]

Size of A after removing duplicate elements: 5
'''

def removeDuplicates(A):
    length = len(A)
    if length==0:
        return 0
    i = 1
    answer = 1
    while i<length:
        if A[i]!=A[i-1]:
            answer+=1
        i+=1
    return answer


print(removeDuplicates([1,2,3, 3, 3, 4, 5, 5]))