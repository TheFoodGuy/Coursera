/* convert this program to cpp 
change to cpp io 
change to one line comments
change defines of constants to const
change array to vector<>
inline any short function */
#include <stdio.h>
#define N 40
void sum (int * p, int n, int d[]){
    int i ;
    *p = 0 ;
    for(i = 0 ; i < n; ++i){
        *p = *p + d[i] ;
    }
}

/* what does this program do:
    it creates an array of size 40, for every loop of the main for loop, 
    it calls the function which adds everything up to the current index and 
    updates everything to accum
*/
int main(){
    int i ; 
    int accum = 0 ; 
    int data[N] ; 
    for(i = 0 ; i < N ; ++i){
        data[i] = i ; 
        sum(&accum, N, data) ; 
    }
    printf("sum is %d\n", accum) ; 
    return 0 ;
}