class Solution {
public:
    int romanToInt(string s) {
        map<char, int> rule;
        rule['I'] = 1;
        rule['V'] = 5;
        rule['X'] = 10;
        rule['L'] = 50;
        rule['C'] = 100;
        rule['D'] = 500;
        rule['M'] = 1000;
        size_t length = s.size();
        int ans = 0;
        for(size_t i=0; i<length-1; i++){
            if(rule[char(s[i])] >= rule[char(s[i+1])]){
                ans += rule[char(s[i])];
            }
            else{
                ans -= rule[char(s[i])];
            }
        }
        ans += rule[char(s[length-1])];
        return ans;
    }
};
