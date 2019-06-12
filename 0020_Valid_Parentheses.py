class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        
        #If input is empty, return true???
        if length==0:
            return True
        
        
        #If length is odd, string must be invalid
        if length%2 == 1:
            return False
        
        #If length is even, use stack to judge
        if length%2 == 0:
            stack = []
            i = 0
            while i < length:
                #If character is left parenthesis, push it into stack
                if s[i]=='(' or s[i]=='[' or s[i]=='{':
                    stack.append(s[i])
                    i += 1
                    continue
                #If character is right parenthesis, pop out the last character in stack 
                if s[i]==')' or s[i]==']' or s[i]=='}':
                    #If stack is already empty with nothing to pop out, return false
                    if stack == []:
                        break
                    #Else, in order for the string to be valid, the last character 
                    #should be corresponding left parenthesis 
                    else:
                        last = stack.pop()
                        if s[i]==')' and last=='(':
                            i += 1
                            continue
                        elif s[i]==']' and last=='[':
                            i += 1
                            continue
                        elif s[i]=='}' and last=='{':
                            i += 1
                            continue
                        else:
                            break
            
            if i==length:
                #Exclude the corner case: string is composed of left parenthesis only
                if s[i-1]=='(' or s[i-1]=='[' or s[i-1]=='{':
                    return False
                else:
                    return True
            else:
                return False
