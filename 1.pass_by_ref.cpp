#include <bits/stdc++.h>
using namespace std;

void passbyref(string k){
    k[0]='p';
    cout << k << endl;
}

int main(){
    string k= "komu";
    passbyref(k);
    cout << k << endl;
    return 0;


}