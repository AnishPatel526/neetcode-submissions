class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {} # {1: 1, 2: 2, 3: 3}

        for num in nums:
            if num in groups:
                groups[num] += 1
            else:
                groups[num] = 1
        sorted_groups = sorted(groups.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_groups[:k]]