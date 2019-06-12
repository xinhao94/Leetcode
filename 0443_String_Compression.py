class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        
        if length == 0:
            return 0
        
        i = 0
        
        while i < len(chars):
            #Initialize variable "count" to 1
            count = 1
            #Place the probe at the first element, and compare the first element 
            #with its next 
            while (i+1)<len(chars) and chars[i]==chars[i+1]:
                #Use variable "count" to record the number of duplicated elements, 
                #and always keep the first and delete all others
                count += 1
                del chars[i+1]
            
            #If the value of the "count" variable is changed, then we know the "while" 
            #loop has been executed, and we need to update the list
            if count != 1:
                #If the number of duplicated element is larger than two digits, then we need
                #to split the number into multiple single characters
                list_count = list(str(count))
                k = 0
                while k < len(list_count): 
                    chars.insert(i+1+k, list_count[k])
                    k += 1
                #Move the probe to the end of newly-inserted element(s)
                i = i+k
            
            #Move the probe one element forward
            i += 1
            #If we reach the last element, we directly break the "while" loop, since there is
            #no "next" element for the last element
            if i == len(chars)-1:
                break
        
        return len(chars)
