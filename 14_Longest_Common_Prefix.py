class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        num_str = len(strs)
        min_char = len(min(strs, key=len))
        j = 0
        
        while j < min_char:
            i = 0
            while i < (num_str-1):
                if strs[i][j] == strs[i+1][j]:
                    i += 1
                    continue
                else:
                    break
            if i == (num_str-1):
                j += 1
                continue
            else:
                break
        
        if j == 0:
            return ""
        else:
            result = ""
            for k in range(j):
                result += strs[0][k]
            return result
