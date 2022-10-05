#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, s):
        i = 0
        j = 0
        ans = 0
        st = set()
        
        while j<len(s):
            
            if s[j] in st:
                while s[j] in st:
                    st.remove(s[i])
                    i += 1
            else:
                ans = max(ans,j-i+1)
            
            st.add(s[j])
            
            j += 1
            
        return ans
        
 Time Complexity :- O(n)
 Space Complexity :- O(n) when all characters are unique in string.
