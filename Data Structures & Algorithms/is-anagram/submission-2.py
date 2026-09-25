class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in s_counts:
                s_counts[char] += 1 # character already exists, increment 1
            else:
                s_counts[char] = 1 # new character found, creates in dict

        for char in t:
            if char in t_counts:
                t_counts[char] += 1
            else:
                t_counts[char] = 1

        return s_counts == t_counts

        
