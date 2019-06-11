class Solution:
    def countAndSay(self, n: int) -> str:
        
        #Define a function that calculates the current item based on its previous item
        def sayPrevious(string):
            length = len(string)
            i = 0
            result = ""
  
            while i < length:
                if i == length-1:
                    result = result + "1" + string[i]
                    break
                else:
                    count = 1
                    j = 1
                    while (i+j)<length and string[i+j]==string[i]:
                        count += 1
                        j += 1
                    result = result + str(count) + string[i]
                    i = i + count
  
            return result

        result = "1"
        if n == 1:
            return result
        else:
            i = 1
            while i < n:
                result = sayPrevious(result)
                i += 1
        return result
