class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif ' ' not in s:
            return len(s)
        else:
            i = -1
            count = 0
            #If there are space characters at the end of the string,
            #move the probe until it reaches a real character or
            #reaches the begining of the string
            while i >= -len(s) and s[i] == ' ':
                i -= 1
            #Record the length of last word in variable "count" until
            #the probe reaches another space character or reaches
            #the begining of the string
            while i >= -len(s) and s[i] != ' ':
                i -= 1
                count += 1
            return count
