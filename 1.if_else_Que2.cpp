/*
Take the age from the user and then decide accordingly

If age < 18,
print -> "not eligible for job"

If age >= 18 and age <= 54,
print -> "eligible for job"

If age >= 55 and age <= 57,
print -> "eligible for job, but retirement soon"

If age > 57
print -> "retirement time"
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int age;
    cin >> age;

    if(age < 18){
        cout << "Job is not eligible";
    }
    // nested if else

    else if ( age <= 57){
        cout << "Eligible for job";

        if ( age >= 55){
            cout << " Retirement soon ";
        }

    }


    /* else if (age <= 54){
        cout << "Job is eligible";
    }

    else if (age <= 57){
        cout << "Job is eligible but near to retirement";

    }
*/
    else {
        cout << "Retirement";
    }
    
    return 0;
}