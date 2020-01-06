class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        bin_a = int(a,2)
        bin_b = int(b,2)
        bin_result = bin(bin_a + bin_b)
        str_result = str(bin_result)[2:]
        return str_result
