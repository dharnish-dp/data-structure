'''
Given a sorted array, check if there exist two numbers whose sum is zero.
A: [-3, 1, 3, 4]
Answer: true

A: [-2, 1, 3, 4]
Answer: false

'''

def hasTwoSumZero(A):
    # add your logic here
    lenght = len(A)
    i = 0
    j = lenght - 1
    answer = 0
    if i==j:
        return False
    while i<j:
        if A[i]>0:
            return False
        if A[j]<0:
            return False
        if abs(A[i])>abs(A[j]):
            i+=1
        elif abs(A[i])<abs(A[j]):
            j-=1
        else:
            return True
    return False


print(hasTwoSumZero([-3, 1, 3, 4]))
print(hasTwoSumZero([-2, 1, 3, 4]))