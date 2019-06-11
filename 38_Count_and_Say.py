class Solution:
    def countAndSay(self, n: int) -> str:
        
        #Define a function that calculates the current item based on its previous item
        def sayPrevious(string):
            length = len(string)
            i = 0
            result = ""
  
            while i < length:
                #Since there's no "next" number for the last number in the string, we deal 
                #with it separately
                if i == length-1:
                    result = result + "1" + string[i]
                    break
                #For all other numbers except the last one, we compare it with its next number
                else:
                    count = 1
                    j = 1
                    #If its next number is the same with itself, we update "count" and move the 
                    #secondary probe("j") further, until the next number is different or reach 
                    #the end of the input string
                    while (i+j)<length and string[i+j]==string[i]:
                        count += 1
                        j += 1
                    #Update the result based on the while loop
                    result = result + str(count) + string[i]
                    #Move the primary probe based on the while loop
                    i = i + count
  
            return result

        result = "1"
        #If we are asked to calculate the first item, we directly return it
        if n == 1:
            return result
        #If we are asked to calculate the No. n item, we calculate it by calling
        #the "sayPrevious(string)" function (n-1) times.
        else:
            i = 1
            while i < n:
                #The "sayPrevious(string) function need to be iterated for (n-1) times
                result = sayPrevious(result)
                i += 1
        return result
