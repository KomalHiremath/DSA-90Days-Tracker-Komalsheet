#include<bits/stdc++.h>
using namespace std; 
/* 
 void print(){
    cout << "Komal" << "-";
}

int sum(int a, int b){
    return a+b;
}

int main(){
    print (); // it calls the print function
    int s =sum(1,5);
    cout << s; // if i write "s" then it will print Komal s instead of Komal 6
return 0;
}  */

/*
    STL--> ALGO
           CONTAINERS --> VECTORS, LIST, SET, MAP, QUEUE, STACK, UNORDERED MAP
           FUNCTIONS
           ITERATORS    */  

// PAIRS

void Pairs(){
    pair<int, int> p={2,5};
    cout << p.first << " " << p.second << "-";

    pair<int, pair <int, int>> q ={1, {2,3}};
    cout << q.first << " " << q.second.first << " " << q.second.second << "-";

               // indices     0       1      2      3
    pair <int, int> arr []= {{1,2}, {3,4}, {5,6}, {7,8}}; 
    cout << arr [1].second; 
 
}

// VECTORS --> dynamic (can alter the size of an array); if the size of any specific DS is unknown we use vector
//     { f1b, f2b, 3, 4}  f--> front, b-->back

void Vectors(){
vector <int> v;
v.push_back(1);
v.emplace_back(2);
    for (size_t i = 0; i< v.size(); ++i) {   // printing elem;   v.size()-->Automatically gets vector length; Hardcoded number-->Fixed loop count, not recommended
        cout << v[i] << " ";
    }
     cout << "\n";


vector<pair <int, int>> vec;
vec.push_back({1,2});              // use { } to create pairs;       SLOWER
vec.emplace_back(5,9);            // directly constructs the pair;   FASTER        
    for (size_t i = 0; i < vec.size(); ++i) {
        cout  << vec[i].first << "," << vec[i].second << " " ;
    }
    cout << "\n";


vector <int> S(5,100);         // 5--> no of times to be printed/size of array
S.push_back(1);               // prints:100 100 100 100 100 1; ^size dynamically even without prior mentioning size in vector S 
    for (size_t i = 0; i < S.size(); ++i) {
        cout << S[i] << " ";       
   }
    cout << "\n";

vector <int> Q(5);   // 5--> no of times to be printed/size of array
    for (size_t i = 0; i < Q.size(); ++i) {
        cout << Q[i] << " ";       
   }
    cout << "\n";


vector <int> S1(5,13);  // 5--> no of times to be printed/size of array
vector <int> S2(S1);    // copies elem of S1 into S2
    for (size_t i = 0; i < S2.size(); ++i) {
        cout << S2[i] << " ";       
   }
    cout << "\n";    
}

void VectorsIterators(){

    // accessing the elements in the vector using iterators
    vector<int> A = {20, 10, 15, 11, 7};
    vector<int>::iterator it = A.begin();                         // iterator to first element                                                                
    cout << (*it)<< " " ;                                        // print 1st pair
    cout<<"\n";
   
     
    it=it+2;                                                            // moves by to indices pos
    cout << (*it) << " ";
    cout<<"\n"; 

    vector<int>::iterator it2 = A.end();                                  // goes outside the 7
    it2--;                                                                // decrease by 1 pos 
    cout << (*it2)<< " "; 
    cout<<"\n";

   cout << A[0] << " " << "or"<<" " << A.at(0);                            //diff ways to print elem
   cout<<"\n";

   cout << A.back() << " ";                                              // prints the last elm
   cout<<"\n";
   
   for (vector<int>::iterator it3= A.begin(); it3!=A.end(); it3++){
    cout <<(*it3)<< " ";
   }
   cout<<"\n";
    // ways to write for loop;       instead of using  "vector<int>::iterator"  use  "auto" it automatically define it datatype
   for (auto it3 = A.begin(); it3 != A.end(); ++it3) {
    cout << *it3 << " ";
}



}

void VectorsDeletion(){
    vector<int> v={10, 20, 30, 40};
    v.erase(v.begin());   // 20,30,40
    v.erase(v.begin()+1); // 20 40 
        for (auto i:v){
        cout<<i<<" ";
    }
    cout <<"\n";

            //index  0   1   2   3   4   5
    vector<int> v1={10, 20, 30, 40, 50, 60};
    // i want to delete 30 and 40
    v1.erase(v1.begin()+2, v1.begin()+4);  // always include the pos of next elem in v1.begin()+4)  [start, end)
        for (auto j:v1){
        cout<<j<<" ";
    }
    


}

void VectorsInsertion(){
    
    vector<int>z1(2,100);
    z1.insert(z1.begin(), 300); // insert at the front
            for (auto i:z1){
        cout<<" "<< i;
    }
    cout<<"\n";  //300 100 100


    vector<int>z2(3,700);
    z2.insert(z2.begin()+1, 213);
        for (auto j:z2){
        cout<< " "<< j ;
    }
    cout<<"\n";
    cout<<"\n";// 700 213 700 700

    vector<int>z3(3,200);
    z3.insert(z3.begin()+1, 2, 13); // 2 is the no of times to be inserted , 13 is given no
        for (auto j:z3){
        cout << " "<< j;
    }
    cout<<"\n"; // 200 13 13 200 200


    // COPYING THE ELEMENTS AND INSERTING
    vector<int>copy(2, 49);
    z3.insert(z3.begin(),copy.begin(), copy.end());
            for (auto j:z3){
        cout << " "<< j;
    }
    cout<<"\n"; //49 49 200 13 13 200 200


    vector<int>z4(3,400);
    z4.insert(z4.end(), 213);
        for (auto j:z4){
        cout << " "<< j;
    }
    cout<<"\n"; //  400 400 400 213

   z2.pop_back();  // 700 213 700 700
   for (auto j:z2){
        cout<< " "<< j ;
    }
    cout<<"\n"; // 700 213 700

    z1.swap(z2);
     for (auto i:z1){
        cout<<" "<< i;
    }
    cout<<"\n"; // 700 213 700 

    vector<int> v={10, 20, 30, 40};
    v.erase(v.begin(), v.end()); // erase entire vector

    cout<<v.empty();  // if empty YES prints 1; NO prints 0 


}

void List() {  // rest all function is same as vector
    list <int> ls = {10, 20, 30, 40};
    ls.push_back(2);
    ls.emplace_back(4);
    
    ls.push_front(7);
    ls.emplace_front(8);

    for (auto i : ls) {
        cout << i << " ";
    }
    cout << endl;
}

void Deque(){  // rest all function is same as vector
    deque<int> dq = {10, 20, 30, 40};
    dq.push_back(2);
    dq.emplace_back(4);
    
    dq.push_front(7);
    dq.emplace_front(8);

    for (auto i : dq) {
        cout << i << " ";
    }
    cout << endl;
}

void Stack(){
    stack<int> st;
    st.push(8);
    st.push(9);
    st.push(0);
    st.push(6);
    st.emplace(7);
      while(!st.empty()){    //  “Continue looping as long as the stack is not empty.”
        cout << st.top() << "->"; // {7 6 0 9 8 }
        st.pop();   // {7}
        cout<< st.size() << ":"; //  Top Printed->Size After Pop:  7->4 6->3 0->2 9->1 8->0
        cout<< st.empty() << "  "; // returns a boolean true = 1, false = 0  7->4:0  6->3:0  0->2:0  9->1:0  8->0:1 
      }
      // for swapping
      stack<int> st1,st2;
      st1.swap(st2);
}

void Queue(){
    queue<int> q;
    q.push(3);
    q.push(1);
    q.push(4);
    q.emplace(2);
    q.back() +=5;
      while(!q.empty()){    //  “Continue looping as long as the queue is not empty.”
      cout<<  q.front() << " ";   // 3 1 4 7(2+5) 
       q.pop();
}
cout<< " back "<<  q.back() ; // 3 1 4 7  back 7 
}

void PriorityQueue(){ // max heap; in descending order
    priority_queue <int> pq;
    pq.push(5); // {5}
    pq.push(2);  // {5,2}
    pq.push(9);  // {9,5,2}
    pq.emplace(1); // // {9,5,2,1}

    while(!pq.empty()){
        cout << pq.top() << " "; // 9 5 2 1 
        pq.pop(); 
    }
     cout << "top is " << pq.top();   // 9 5 2 1 top is 1     
}

void PriorityQueuemin(){ // min heap; in ascending order
    priority_queue <int, vector<int>, greater<int>> pq;
    pq.push(5); // {5}
    pq.push(2);  // {2,5}
    pq.push(9);  // {2,5,9}
    pq.emplace(1); // // {1,2,5,9}

    while(!pq.empty()){
        cout << pq.top() << " "; // 1 2 5 9 
        pq.pop();
    }  
}

// ❌ ✔️
void Set(){     // SORTED(✔️) UNIQUE(✔️)       // begin(), end(), rbegin(), rend(), size(),empty() and swap() are same as those of above

    set<int> st;
    st.insert(1);  //1
    st.insert(2);  //1 2
    st.emplace(2); // 1 2 --> stores unique ONLY
    st.insert(4);  // 1 2 4
    st.insert(3);  // 1 2 3 4 // SORT ITSELF
    st.insert(5);  // 1 2 3 4 5 

    for (auto val:st){
    cout<< val<< " ";
   }cout <<endl;

    //To find any element in the set
    auto val= st.find(9); 
    if (val !=st.end()){ // "If we didn’t reach the end, it means elem was found in the set."
        cout<< " Element found"<< endl;
    }else{
         cout << " Element not  found"<< endl;
    }
   
    auto result =st.erase(1);
    cout << "1 if erased 0 not erased: "<< result<< endl;

    auto cnt= st.count(2);
    cout << "Counts if element is P(1) AB(0): "<< cnt;
    cout<< endl;

    // IF I WANT TO DELETE 2 ELEM FOLLOW VECTOR [START, END)
    set<int> s = {1, 2, 3, 4 ,5}; // DELETE 2 3 
    auto it1=s.find(2);
    auto it2=s.find(4);
    s.erase(it1,it2);

    for (auto x: s){
        cout << x<< " ";
    }
    cout <<endl;
}

void MultiSet(){  // SORTED(✔️) UNIQUE(❌)  SAME AS SET

    multiset<int> ms;
    ms.insert(1);  //1
    ms.insert(2);  //1 2
    ms.emplace(2); // 1 2 2
    ms.insert(4);  // 1 2 2 4
    ms.insert(4); //1 2 2 4 4 
     ms.insert(4); //1 2 2 4 4 4
    ms.insert(3);  //1 2 2 3 4 4 4   SORT ITSELF
    ms.insert(5);  // 1 2 3 4 4 4 5 

    for (auto val:ms){
    cout<< val<< " ";
   }cout <<endl;

    //To find any element in the set
    auto val= ms.find(9); 
    if (val !=ms.end()){ // "If we didn’t reach the end, it means elem was found in the set."
        cout<< " Element found"<< endl;
    }else{
         cout << " Element not  found"<< endl;
    }
   
    auto result =ms.erase(1); // erase all 1 present in the multiset
    cout << "1 if erased 0 not erased: "<< result<< endl;

    ms.erase(ms.find(4)); // erases only ONE occurrence of 4 from the multiset.
       for (auto val : ms) {
        cout << val << " ";
    }
 


}

void UnorderedSet() {  SORTED(❌) UNIQUE(✔️)
    unordered_set<int> st;
    // lower_bound and upper_bound function does not work, 
    //rest all functions are same
    //  It has a better complexity than set in most cases, except some when collision happens
}



int main(){
    MultiSet();
    return 0;

}

