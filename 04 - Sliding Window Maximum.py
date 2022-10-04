class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = []
        
        i = 0
        j = 0 
        ans = []
        
        while j<len(nums):
            
            while q and q[-1]<nums[j]:
                q.pop()
            
            q.append(nums[j])
            
            if j-i+1 < k:
                j += 1
                
            elif j-i+1 == k:
                
                ans.append(q[0])
                
                if q[0] == nums[i]:
                    q.pop(0)
                    
                i += 1
                j += 1
        
        return ans 
            
 Time complexity : - O(n)
 Space Complexity : - O(k)
