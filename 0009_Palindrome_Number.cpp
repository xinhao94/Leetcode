class Solution {
public:
    bool isPalindrome(int x) {
        bool ans = true;
        if(x<0){
            ans = false;
            return ans;
        }
        int length = int(log10(x))+1;
        for(int i=1; i<=int(length/2); i++){
            int tail = int(x/(int(pow(10, i-1)))) % 10;
            int head = int(x/(int(pow(10, length-i)))) % 10;
            if(tail != head){
                ans = false;
                break;
            }
        }
        return ans;
    }
};
