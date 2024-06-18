#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    static bool algo(int n)
    {
        if(n==0){ return false; }

        int reverse = 0;
        int temp = n;

        while (temp != 0)
        {
            int digit = temp % 10;
            reverse = reverse * 10 + digit;
            temp /= 10;
        }

        return (reverse == n);
    }
};

int main()
{
    cout<<  Solution::algo(121) << endl;
    return 0;
}