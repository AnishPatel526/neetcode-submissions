class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1

        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return nums[m]
        #     elif nums[m]

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
