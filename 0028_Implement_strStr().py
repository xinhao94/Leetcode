class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if haystack == '':
            return -1
        
        len_h = len(haystack)
        len_n = len(needle)
        if len_n > len_h:
            return -1
        i = 0
        # Run the while loop only when the remaining of haystack is longer than needle 
        while (len_h - i) >= len_n:
            if haystack[i] != needle[0]:
                i += 1
                continue
            else:
                j = 0
                while (j < len_n) and ((i+j) < len_h): 
                    if haystack[i+j] == needle[j]:
                        j += 1
                        continue
                    else:
                        break
                if j == len_n:
                    return i
                    break
                else:
                    i += 1
                    continue
        return -1
