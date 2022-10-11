class Solution {
public:
     int mod = 1e9+7;
    int validPaths(vector<vector<int>>&grid,int k, int row, int col,int sum,vector<vector<vector<int>>>&dp){
        if(row<0||col<0||row>=grid.size()||col>=grid[0].size())
            return 0;
        if(row==grid.size()-1&&col==grid[0].size()-1){
            sum+=grid[row][col];
            if(sum%k==0)
                return 1;
            return 0;
        }
        if(dp[row][col][sum%k]!=-1)
            return dp[row][col][sum%k];
        long down=validPaths(grid,k,row+1,col,sum+grid[row][col],dp);
       long right=validPaths(grid,k,row,col+1,sum+grid[row][col],dp);
        return dp[row][col][sum%k]=(down%mod+right%mod)%mod;         
    }
    int numberOfPaths(vector<vector<int>>& grid, int k) {
    vector<vector<vector<int>>>dp(grid.size(),vector<vector<int>>(grid[0].size(),vector<int>(51,-1)));
        return validPaths(grid,k,0,0,0,dp);
    }
};
