class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        
        if length == 0:
            return 0
        
        i = 0
        
        while i < len(chars):
            count = 1
            while (i+1)<len(chars) and chars[i]==chars[i+1]:
                count += 1
                del chars[i+1]
            
            if count != 1:
                list_count = list(str(count))
                k = 0
                while k < len(list_count): 
                    chars.insert(i+1+k, list_count[k])
                    k += 1
                i = i+k
            
            i += 1
            if i == len(chars)-1:
                break
        
        return len(chars)
