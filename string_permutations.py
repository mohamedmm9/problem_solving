class Solution:
    def checkInclusion(self,s1,s2):
        len_s1 = len(s1)
        len_s2 = len(s2)
        from collections import Counter
        counterS1 = Counter(s1)
        counterW = Counter(s2[:len_s1-1])
        for i in range(len_s1-1, len_s2):
            st_idx = i-(len_s1-1)
            counterW[s2[i]] += 1
            if counterW == counterS1:
                return True
            counterW[s2[st_idx]] -= 1
            if counterW[s2[st_idx]] == 0:
                counterW.pop(s2[st_idx])
        return False
