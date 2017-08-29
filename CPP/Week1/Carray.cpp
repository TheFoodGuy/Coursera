/* 
David Liang - first programming assignment from coursera 
C++ programming from C kind of suff - CS109 in a way
this is the cpp version of C array in vectors instead
*/
#include <iostream>
#include <vector> 
using namespace std ; 
const int N = 40 ; 
// this is to sum up the integers in the array.
inline void sum(int &accum, int n, vector<int> d){
    int i ; 
    accum = 0 ; 
    for(i = 0 ; i < n; ++i){
        accum = accum + d[i] ; 
    }
}

int main(){
    int i ; 
    int accum ; 
    vector<int> data ; 
    for (i = 0 ; i < N ; ++i){
        data.push_back(i); 
        sum(accum, N, data) ; 
    }
    cout << "sum is " << accum << endl ; 
    return 0 ; 
}