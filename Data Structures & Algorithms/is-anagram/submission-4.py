class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        for j in t:
            freq[j] -= 1
            if freq[j] < 0:
                return False
        return True
