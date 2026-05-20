class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_freq, t_freq = defaultdict(int), defaultdict(int)
        for i in s:
            s_freq[i] += 1
        for j in t:
            t_freq[j] += 1

        ana = False
        for k, v in s_freq.items():
            if s_freq[k] == t_freq[k] or t_freq[k] == s_freq[k]:
                ana = True
            else:
                ana = False
                break
        return ana
