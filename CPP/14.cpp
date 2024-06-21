#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string static longestCommonPrefix(vector<string>& strs) {
        
        if(strs.size() == 1)
            return strs[0];
        
        string final = "";
        int count = 0;

        for(int i=1; i <= strs.size()-1; i++){

            string prefix = strs[0];
            final = "";
            count = 0;

            if(strs[i] == "")
                return "";

            while( true ){
                string word = strs[i];
                if( prefix[count] == word[count]){
                    final = final + prefix[count];
                    count++;
                }else
                    break;
            }
        }
        return final;
    }
};



int main(){

    vector<string> strs {"flower","flower","flower","flower"};
    cout <<  Solution::longestCommonPrefix(strs) << endl;


    return 0;
}

// Solution from Leetcode Soln Section
// class Solution {
// public:
//     string static longestCommonPrefix(vector<string>& v) {
//         string ans="";
//         std::sort(v.begin(),v.end());
//         int n=v.size();
//         string first=v[0],last=v[n-1];
//         for(int i=0;i<min(first.size(),last.size());i++){
//             if(first[i]!=last[i]){
//                 return ans;
//             }
//             ans+=first[i];
//         }
//         return ans;
//     }
// };