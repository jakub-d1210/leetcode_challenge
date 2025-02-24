class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i] #return index of solutions
            hash_map[num] = i #add index to dictionary
            
        return [] #if we have not found solution


#test data from LeetCode
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twosum(nums,target))

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]     

