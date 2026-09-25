class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # maps value -> index for O(1) lookups
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            
            # the exact number we need to pair with num to reach target
            complement = target - num

            # if we've seen the complement before, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # haven't found a pair yet, store this number for future iterations
            seen[num] = i