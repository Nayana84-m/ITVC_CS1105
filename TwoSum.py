# LeetCode Problem: Two Sum
# Lab 5 – ITVC CS1105

def twoSum(nums, target):
    num_index = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_index:
            return [num_index[complement], i]

        num_index[nums[i]] = i


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
