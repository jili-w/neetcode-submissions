class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int two = 2;
        while(two--){
            for(int n: nums){
                ans.push_back(n);
            }
        }
        return ans;
    }
};