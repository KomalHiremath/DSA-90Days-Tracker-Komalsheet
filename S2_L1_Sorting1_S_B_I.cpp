#include<bits/stdc++.h>
using namespace std;
/*
Analogy:

i is like the manager giving instructions.
j is like the employee doing the actual sorting/merging/finding.

In Any Nested Loop Code:

i gives the limits
j executes the logic inside that limit                 */

void selection_sort(int arr[], int n){
    for (int i=0; i<=n-2; i++){
        int mini=i;
        for (int j=i; j<=n-1; j++){
            if (arr [j] < arr[mini]){
                mini =j;
            }
        }
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i]= temp;
    }
}

void bubble_sort(int arr [], int n){
    for (int i=n-1; i>=0; i--){
        int didSwap = 0;
        for (int j=0; j<=i-1; j++){   // so we must stop at j = i - 1 becoz arr[j + 1] must not go out of bounds.
            if (arr[j] > arr[j+1]){  // Swap if left element is greater than right  || j is the current elem and j+1 is the adjacent elem of j
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                didSwap = 1;
            }
        }
        if (didSwap == 0){
            break;
        }
        cout << "The number of times the loop ran\n";

    /*
5 
7 3 4 6 1
The number of times the loop ran
The number of times the loop ran
The number of times the loop ran
The number of times the loop ran
1 3 4 6 7

5
1 2 3 4 5
1 2 3 4 5 
*/
    }
}

void insertion_sort(int arr [], int n){
    for(int i =0; i<=n-1; i++){  // Start from 0 and go till the end of the array
        int j =i;  // j will help in shifting the element to its correct position
        while (j >0 && arr[j-1] > arr[j]){  // While j is not the first index && the previous element is bigger
            int temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = temp;
            j--; // Move left to keep checking where to place current element
            cout << "loops run\n"; // Just to show how many times this inner loop runs
        }
    }
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; i++) cin >> arr[i];
    insertion_sort(arr, n);
    for (int i=0; i<n; i++){
        cout <<arr[i]<< " ";
    }

}