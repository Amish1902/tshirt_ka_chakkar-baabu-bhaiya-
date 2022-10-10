class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target)
    {
        if(nums.size()==0)
        {
            return {-1,-1};
        }
        int i,j,mid;
        i=0;
        j=nums.size()-1;
        int left=-1,right=-1;
        
        while(i<=j)
        {
            mid=(i+j)/2;
            if(nums[mid]>target)
            {
                j=mid-1;
                
            }else if(nums[mid]<target)
            {
             i=mid+1;
            }else
            {
                left=mid;
                j=mid-1;
            }
        }
         i=0;
        j=nums.size()-1;
        while(i<=j)
        {
            mid=(i+j)/2;
            if(nums[mid]>target)
            {
                j=mid-1;
                
            }else if(nums[mid]<target)
            {
             i=mid+1;
            }else
            {
                right=mid;
                i=mid+1;
            }
        }
        vector<int>ans;
        ans.push_back(left);
        ans.push_back(right);
        return ans;
    }
};
