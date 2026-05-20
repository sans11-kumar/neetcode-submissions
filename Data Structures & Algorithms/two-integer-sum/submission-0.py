class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return None
       
        seen = {}

        for i, j in enumerate(nums):
            complement = target - j
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[j] = i
        