/*
Functions are set of code which performs something for you  
Functions are used to modularise code  
Functions are used to increase readability  
Functions are used to use same code multiple times  
void -> which does not returns anything  
return  
parameterised  
non parameterised
*/

#include <bits/stdc++.h>
using namespace std;


    void printname(string name){
        cout<< "Hello" << name << endl;
    }

    int main (){
        string name;
        cin >> name;
        printname(name);

        string name1;
        cin >> name1;
        printname(name1);
    
        return 0;
    } 
