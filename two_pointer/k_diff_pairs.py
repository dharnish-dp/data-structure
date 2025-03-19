'''
k-diff pairs
Medium
50 / 50
Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.

|arr[i] - arr[j]| = k where i < j
'''

def k_diff_pair(A,k):
    count,i,j,length = 0,0,1,len(A)
    data = set()
    while j<length:
        if i==j or A[j]-A[i]<k:
            j+=1
        elif A[j]-A[i]>k:
            i+=1
        else:
            if (A[i],A[j]) not in data:
                count+=1
                data.add((A[i],A[j]))
            i+=1
            j+=1
    return count

print(k_diff_pair([1, 3, 5, 7, 10],2))
print(k_diff_pair([1, 3, 5, 7, 10],3))
print(k_diff_pair([1, 3, 5, 7, 10],1))