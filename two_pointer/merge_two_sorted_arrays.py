'''
Given two sorted arrays A and B, find the merged sorted array C by merging A and B.

Example:
A: [1, 2, 3, 4, 4]
B: [2, 4, 5, 5]
C: [1, 2, 2, 3, 4, 4, 4, 5, 5]

'''


def merge_two_sorted_arrays(A, B):
    C = []
    a_len = len(A)
    b_len = len(B)
    i = 0
    j = 0
    while i<a_len and j<b_len:
        if A[i]<B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1
        else:
            C.append(A[i])
            C.append(B[j])
            i+=1
            j+=1
    if i<a_len:
        C = C+A[i:]
    if j<b_len:
        C = C+B[j:]
    return C

A = [1, 2, 3, 4, 4]
B = [2, 4, 5, 5]
print(merge_two_sorted_arrays(A, B)) 