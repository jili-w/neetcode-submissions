class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for (const auto& s : strs) {
            vector<int> ponder(26, 0);        // ✅ outside inner loop
            for (char c : s) {
                ponder[c - 'a']++;
            }

            string key = to_string(ponder[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(ponder[i]);
            }

            res[key].push_back(s);
        }

        vector<vector<string>> result;
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};