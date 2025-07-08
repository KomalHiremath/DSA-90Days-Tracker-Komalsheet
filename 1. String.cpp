#include <bits/stdc++.h>
using namespace std;
int main() {
    string s = "Komal";
    int len = s.size(); // get the length of the string
    s[len-3] = 'a';    // change the 3rd last character to 'a'
    cout << s[len-3];  // print the replaced string
    cout << s;        // print the new char
    return 0;

}