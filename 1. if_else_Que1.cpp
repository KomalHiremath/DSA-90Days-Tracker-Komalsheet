/*
A school has following rules for grading system:
a. Below 25 – F 
b. 25 to 44 – E 
c. 45 to 49 – D 
d. 50 to 59 – C 
e. 60 to 79 – B 
f. 80 to 100 – A
Ask user to enter marks and print the corresponding grade.
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    int marks;
    cin >> marks;
    if ( marks < 24){
        cout << "F";
    }

     else if ( marks <= 44){
        cout << "E";
    }

    else if (marks <= 49){
        cout << "D";
    }

     else if ( marks <= 59){
        cout << "C";
    }

    else if ( marks <=79){
        cout << "B";
    }

    else if ( marks <= 100){
        cout << "A";
    }
    return 0;

}