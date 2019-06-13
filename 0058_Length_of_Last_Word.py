class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif ' ' not in s:
            return len(s)
        else:
            i = -1
            count = 0
            while i >= -len(s) and s[i] == ' ':
                i -= 1
            while i >= -len(s) and s[i] != ' ':
                i -= 1
                count += 1
            return count
