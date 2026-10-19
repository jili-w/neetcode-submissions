class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        for(const string& s : strs){
            encoded +=  to_string(s.size()) +"#" + s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i <s.size()){
             int j = i;
             while(s[j] != '#'){
                    j++;
             }
             //we get the number with this line (j-1 is incase its more than 1 integer (23,21))
             int length = stoi(s.substr(i, j - i));

             // now we can set the distance between each encoded string
             i = j+1;
             j = i+length ;

             res.push_back(s.substr(i,length));
             i = j;
        
        }
        return res;

    }
};
