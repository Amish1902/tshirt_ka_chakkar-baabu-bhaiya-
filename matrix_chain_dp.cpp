#include <iostream>
#include <limits.h>
using namespace std;

int mChain(int p[], int n) 
{ 
  
    int dp[n][n];
    for (int i=0; i<n-1; i++)
       dp[i][i+1] = 0;
       
    for (int gap = 2; gap < n; gap++)
    {
        for (int i=0; i+gap < n; i++)
        {
            int j = i + gap;
            dp[i][j] = INT_MAX;
            for (int k=i+1; k<j; k++)
            {
               dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + p[i]*p[k]*p[j]);
            }
        }     
    }
    
    return dp[0][n-1];
}

int main() {
    
    	int n = 4, arr[]= {2, 1, 3, 4};
    	
    	cout<<mChain(arr, n);
    	
    	return 0;
}