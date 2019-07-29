class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        size_t length = nums.size();
        int ans1 = 0;
        int ans2 = 0;
        bool loop = true;
        for(size_t i=0; i<length; i++){
            for(size_t j=i+1; j<length; j++){
                if(nums[i] + nums[j] == target){
                    ans1 = i;
                    ans2 = j;
                    loop = false;
                    break;
                }
            }
            if(loop == false){
                break;
            }
        }
        vector<int> ans(2);
        ans[0] = ans1;
        ans[1] = ans2;
        return ans;
    }
};
