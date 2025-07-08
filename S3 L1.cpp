// find the Largest element in an Array
#include <bits/stdc++.h>
using namespace std;
int largestElement (vector <int> &arr, int n ){
    int largest= arr [0]; //global declaration of largest element
    for (int i=0; i<n; i++){
        if(arr[i]>largest){
            largest=arr[i];
        }
    }
     return largest;
}
int main() {
    vector<int> arr = {5, 7, 2, 9, 1};
    int n = arr.size();
    cout << "Largest element is: " << largestElement(arr, n) << endl;
    return 0;
}