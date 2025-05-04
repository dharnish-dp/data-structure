'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''

def squares_of_a_sorted_array(nums):
    # Initialize result array to store squared numbers
    result = []
    # Initialize two pointers: i at start and j at end
    i = 0
    j = len(nums)-1
    
    # Use two-pointer approach to compare absolute values
    # This works because the array is sorted, so largest squares will be at the ends
    while i < j:
        # Compare absolute values to handle negative numbers
        if abs(nums[i]) > abs(nums[j]):
            # If left pointer has larger absolute value, square it and add to start of result
            result.insert(0, nums[i]**2)
            i += 1
        elif abs(nums[i]) < abs(nums[j]):
            # If right pointer has larger absolute value, square it and add to start of result
            result.insert(0, nums[j]**2)
            j -= 1
        else:
            # If both pointers have equal absolute values, add both squares
            # Need to add them in correct order to maintain sorting
            result.insert(0, nums[j]**2)  # Add right pointer first
            result.insert(0, nums[i]**2)  # Then add left pointer
            i += 1
            j -= 1
    
    # Handle the case when i and j meet (middle element)
    if i == j:
        result.insert(0, nums[j]**2) 
    return result

print(squares_of_a_sorted_array([-4,-1,0,3,10]))