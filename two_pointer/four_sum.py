'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Time Complexity: O(n^3)
Space Complexity: O(1) excluding the space for output
'''

def fourSum(nums, target):
    # Sort array to handle duplicates and use two-pointer technique
    nums.sort()
    result = []
    n = len(nums)
    
    # Fix first two numbers and use two pointers for remaining two
    for i in range(n - 3):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        for j in range(i + 1, n - 2):
            # Skip duplicates for second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            # Use two pointers for remaining two numbers
            left = j + 1
            right = n - 1
            
            # At this point:
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a valid quadruplet
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for third number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for fourth number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
    return result

# Test cases
print(fourSum([1,0,-1,0,-2,2], 0))  # Expected: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2,2,2,2,2], 8))      # Expected: [[2,2,2,2]]

