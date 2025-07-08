#include <bits/stdc++.h>
using namespace std;

void passbyval(string k){
    k[0]='p';
    cout << k << endl;
}

int main(){
    string k= "komu";
    passbyval(k);
    cout << k << endl;
    return 0;


}