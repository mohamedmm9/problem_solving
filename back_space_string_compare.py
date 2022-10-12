class Solution:
    def removal(self, s):
        sChanged = ""
        sRemoval = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#':
                sRemoval += 1
            elif sRemoval > 0:
                sRemoval -= 1
            else:
                sChanged = s[i] + sChanged
        return sChanged
    def backspaceCompare(self, s, t):
        sChanged = self.removal(s)
        tChanged = self.removal(t)
        return sChanged == tChanged
