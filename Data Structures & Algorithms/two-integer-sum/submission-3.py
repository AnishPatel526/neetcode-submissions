class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num # tells you exactly what number you are looking for

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i