#include <iostream>
using namespace std;

int main(){

    int a = 98321;
    int b = 39210;

    cout << "Before Swap: " << endl;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    a = a^b;
    b = a^b;
    a = a^b;

    cout << "After Swap: " << endl;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;


    return 0;
}