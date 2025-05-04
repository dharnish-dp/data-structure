'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge(intervals):
    intervals.sort(key = lambda i: i[0])
    output = [intervals[0]]
    for start,end in intervals[1:]:
        if output[-1][1]>=start:
            output[-1][1] = max(end,output[-1][1])
        else:
            output.append([start,end])
    return output

# Test cases
result = merge([[1,3],[2,6],[8,10],[15,18]])
print(result) # [[1,6],[8,10],[15,18]]
result = merge([[1,4],[4,5]])
print(result) # [[1,5]]
result = merge([[1,4],[2,3]])
print(result) # [[1,4]]
result = merge([[1,4],[0,4]])
print(result) # [[0,4]]