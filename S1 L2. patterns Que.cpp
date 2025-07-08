#include <bits/stdc++.h>
using namespace std;

 /*int main(){

   int i, j;
     for (i=0; i<4; i++){
        for (j=0; j<4; j++){
            cout << "*";
        }
        cout << endl;

     }  
     }*/ // written by me

void print0 (int n) {
        for (int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cout << "* ";
            }
             cout << endl;
        }
     } /*
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *        */

void print1(int n) {
        for (int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                cout << "* ";
            }
             cout << endl;
        }
     }/*
* 
* *
* * *
* * * *
* * * * *                 */

void print2(int n) {
        for (int i=1; i<=n; i++){
            for(int j=1; j<=i; j++){
                cout << j << " ";
            }
             cout << endl;
        }
     }  /*
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5                  */

void print3(int n) {
        for (int i=1; i<=n; i++){
            for(int j=1; j<=i; j++){
                cout << i << " ";
            }
             cout << endl;
        }
     } /* 
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5                */

void print4(int n) {
        for (int i=1; i<=n; i++){
            for(int j=1; j<=n-i+1; j++){
                cout << "*-";
            }
             cout << endl;
        }
     } /*
*-*-*-*-*-
*-*-*-*-
*-*-*-
*-*-
*-                        */
     
void print5(int n) {
        for (int i=1; i<=n; i++){
            for (int j=1; j<=n-i+1; j++){
                cout << j << "";
            }
            cout << endl;
        }
     }/*  
12345
1234
123
12
1                      */

void print6(int n){


        for (int i=0; i<n; i++){
            for (int j=0; j<n-i-1; j++){ //space
                cout << "-";
            }
                for(int j=0; j<2*i+1; j++){ //star
                    cout << "*";
                }
                for (int j=0; j<n-i-1; j++){ //space
                cout << "-";
            }
            cout<<endl;
        }

     }/*
        
----*----
---***---
--*****--
-*******- 
*********              */
      
void print7(int n){
           for (int i=0; i<n; i++){
            for (int j=0; j<i; j++){ //space
                cout << "-";
            }
                for(int j=0; j<2*n - (2*i + 1); j++){ //star
                    cout << "*";
                }
                for (int j=0; j<i; j++){ //space
                cout << "-";
            }
            cout<<endl;
        }

     }/*
*********
-*******-
--*****--
---***---
----*----           */

/*void print8(int n){
        for (int i=1; i<=n; i++){
            for (int j=1; j<i+1; j++){
                cout << "*";
            }
            for (int j=1; j<n-1; j++){
                cout << "-";
            }
            cout<< endl;
        
        }
    }
         void print9(int n){
        for (int i=1; i<n; i++){
            for (int j=1; j<6-i; j++){
                cout << "*";
            }
            for (int j=1; j<i+1; j++){
                cout << "-";
            }
            cout << endl;
        } } */ // this code was written by me it is hardcoded and not dynamic so it is not good practice to write code like this.
   
void print8(int n){
            for (int i=1; i<=2*n-1; i++){
               int stars= i;
               if(i>n) stars= 2*n-i;
               for(int j=1; j<=stars; j++ ){
                cout << "*";
               }
               cout << endl;
            }
          }/*
          
*          
** 
***
****
*****
****
***
**
*                       */

void print9(int n){
            int start =1;
            for (int i=0; i<n; i++){
                if (i%2==0) start=1;
                else start = 0;
                for (int j=0; j<=i; j++){
                    cout << start;
                    start= 1-start;
                }
                cout << endl;
        }
    }/*
1
01
101
0101
10101                   */
      
void print10 (int n){
    int space=2*(n-1);
    for (int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){ //for the numbers
            cout << j;
        }

        for (int j=1; j<=space; j++){ //for the spaces
            cout << "-";
    }
     for(int j=i; j>=1; j--){ //for the numbers
            cout << j;
        }
        cout << endl;  
         space -= 2; // or space= space-2
          
    }
}/*
1------1
12----21
123--321
12344321          */
   

void print11 (int n){
    int num=1;
    for (int i=1; i<=n; i++){
        for (int j=1; j<=i; j++){
            cout << num << "-";
            num =num +1; // num++
        }
        cout << endl;
    }
} /*
1-
2-3-
4-5-6-
7-8-9-10-
11-12-13-14-15-        */

void print12 (int n){
    for (int i=1; i<=n; i++){
        for (char ch='A'; ch< 'A' + i; ch++){
        cout << ch << "-";
        }
        cout << endl;
    }
}/*
A-
A-B-
A-B-C-
A-B-C-D-
A-B-C-D-E-         */

void print13 (int n){
    for (int i=0; i<n; i++){
        for (char ch='A'; ch<= 'A' + (n-i-1); ch++){
        cout << ch << "-";
        }
        cout << endl;
    }
}/*
A-B-C-D-E-
A-B-C-D-
A-B-C-
A-B-
A-            */

void print14 (int n){
    for (int i=0; i<n; i++){
        char ch= 'A' + i;
        for (int j=0; j<=i ; j++){
        cout << ch << "-";
        }
        cout << endl;
    }
}/*
A-
B-B-
C-C-C-
D-D-D-D-
E-E-E-E-E-       */

void print15 (int n){


        for (int i=0; i<=n; i++){
            for (int j=0; j<n-i-1; j++){ //space
                cout << "-";
            } 
            char ch= 'A';
            int breakpoint =(2*i+1)/2;
                for(int j=1; j<=2*i+1; j++){ //characters
                    cout << ch ;
                    if (j <=breakpoint)ch++;
                    else ch--;
                }
                for (int j=0; j<n-i-1; j++){ //space
                cout << "-";
            }
            cout<<endl;
        }

     }/*
----A----
---ABA---
--ABCBA--
-ABCDCBA-
ABCDEDCBA                */

void print16 (int n){
    for (int i=0; i<n; i++){
        for (char ch='E' - i; ch <= 'E'; ch++){
            cout << ch << "-";
        }
        cout<< endl;
        }
} /*
E-
D-E-
C-D-E-
B-C-D-E-
A-B-C-D-E-                          */

void print17 (int n){
     int iniS=0 ;
    for (int i=0 ; i<n; i++){    
                            //stars
        for (int j=1; j<=n-i; j++){
            cout << "*";
        }
        for( int j=0; j<iniS; j++){
            cout << "-" ;             //spaces
        }
        for (int j=1; j<=n-i; j++){   //stars
            cout << "*";
        }
        iniS += 2;
        cout<< endl;
    }

    int inis= 2*(n-1) ;
    for (int i=1 ; i<=n; i++){    
                            //stars
        for (int j=1; j<=i; j++){
            cout << "*";
        }
        for( int j=0; j<inis; j++){
            cout << "-" ;             //spaces
        }
        for (int j=1; j<=i; j++){   //stars
            cout << "*";
        }
        inis -= 2;
        cout<< endl;
    }
}/*
**********
****--****
***----***
**------**
*--------*
*--------*
**------**
***----***
****--****
**********           */

void print18 (int n){
    int space=2*n-2;  // when the stars gets decreasing
    for(int i=1; i<=2*n-1; i++){
          int stars=i;
    if (i>n) stars=2*n-i;
        for(int j=1; j<=stars; j++){       // stars
            cout << "*";
    }
    for (int j=1; j<= space; j++){       // spaces
        cout << "-";
    }
    for(int j=1; j<=stars; j++){        // stars
            cout << "*";
}
cout << endl;
if(i<n) space -=2; // when the stars gets increasing
else space +=2; // when the stars gets decreasing
}
}/*
*--------*
**------**
***----***
****--****
**********
****--**** // int space=2*n-2;  // when the stars gets decreasing
***----***
**------**
*--------*                              */

void print19 (int n){
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (i==0 || i==n-1 || j==0 ||j==n-1)
            cout << "*";
            else cout << "-";
        }
        cout << endl;
    }
}/*
*****
*---*
*---*
*---*
*****          */

void print20(int n){
    for (int i=0; i<2*n-1; i++){
        for (int j=0; j<2*n-1; j++){
            int top=i;
            int left=j;
            int right=(2*n-2)-j;
            int bottom= (2*n-2)-i;
            cout << (n-min(min(top, bottom), min(left,right))); //because the numbers are the minimum of the top, left, right, bottom
        }
        cout << endl;
    }
}/*
4444444
4333334
4322234
4321234
4322234
4333334
4444444     */

void print21(int n){
    for (int i=0; i<n; i++){

   
for (int j=0; j<i; j++){
cout << " ";
}
for (int j=0; j<n-i; j++){
    cout << i+1; // it starts with 1 ; if i use just i it will start with 0
}
cout << endl;
 }
}
int main() {
        int n;
        cin >> n;
            print21 (n);
        }



          
// "-" to represent the space
// int num = 5;    num = num + 1;  num is now 6
// int num = 5;    num += num;     num = num + num => 5 + 5 = 10
