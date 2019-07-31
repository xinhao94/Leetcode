class Solution {
public:
    int reverse(int x) {
        if(x == 0){
            return 0;
        }
        if(x == -pow(2,31)){
            return 0;
        }
        bool invert = false;
        if(x < 0){
            x = -x;
            invert = true;
        }
        int length = int(log10(x))+1;
        vector<int> vec(length);
        for(int i=0; i<length; i++){
            vec[i] = x%10;
            x = int(x/10);
        }
        int ans = 0;
        for(int i=0; i<length; i++){
            ans += vec[length-i-1]*pow(10,i);
        }
        // This indicates "ans" has been overflowed
        if(ans == -pow(2,31)){
            return 0;
        }
        else{
            if(invert == false){
                return ans;
            }
            else{
                return -ans;
            }
        }
    }     
};
