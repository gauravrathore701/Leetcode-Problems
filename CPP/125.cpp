#include <iostream>
using namespace std;

class Solution
{
public:
    static bool algo(string n)
    {
        string s = "";
        string o = "";
        for (int i = n.size(); i>=0; i--){
            int a = n[i];
            if( (a > 64) && (a < 91) || ((a > 96) && (a<123)) || ((a > 47) && (a < 58)) )
                s+=tolower(n[i]);

            int b = n[n.size()-i];
            if( (b > 64) && (b < 91) || ((b > 96) && (b<123)) || ((b > 47) && (b < 58)) )
                o+=tolower(n[n.size()-i]);
            
        }
        cout << "o: " << o << endl;
        cout << "a: " << s << endl;
        if(o == s)
            return true;
        else
            return false;
    }
};

int main(){
    cout << Solution::algo("A man, a plan, a canal: Panama") << endl;
    return 0;
}