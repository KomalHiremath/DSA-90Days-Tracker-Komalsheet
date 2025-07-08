// take two numbers and print sum

#include <bits/stdc++.h>
using namespace std;

/*int main(){
    int num1, num2 ;
    cin >> num1 >> num2;
    int sum= num1 + num2;
    cout << sum; 
    return 0;
}*/

//use of return function

int sum(int num1, int num2){
    int num3=num1 + num2; // 5+6=11
    return num3;
}


int main(){
    int num1,num2;
    cin >> num1 >> num2;
    int result =sum (num1, num2);//11
    cout<< result;
    return 0;

}