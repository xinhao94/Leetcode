class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #If input string is empty, return empty string
        if strs == []:
            return ""
        num_str = len(strs)
        #Get the shortest string in the list, the length of which cannot be exceeded by common prefix
        min_char = len(min(strs, key=len))
        #"j" records the length of the prefix
        j = 0
        
        while j < min_char:
            i = 0
            #Compare the first character of each string
            while i < (num_str-1):
                if strs[i][j] == strs[i+1][j]:
                    i += 1
                    continue
                else:
                    break
            #If the first character of all strings is the same, compare the next
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
