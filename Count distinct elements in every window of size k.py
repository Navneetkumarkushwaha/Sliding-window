class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, k):
        
        i = 0
        j = 0
        ans = []
        dic = dict()
        
        while j < len(A):
            
            if A[j] in dic:
                dic[A[j]] += 1
            else:
                dic[A[j]] = 1
                
                
            if (j-i+1) == k:
                
                ans.append(len(dic))
                dic[A[i]] -= 1
                
                if dic[A[i]] == 0:
                    del dic[A[i]]
                
                i += 1
            j  += 1
                
        return ans
                
Time complexity: O(N), A single traversal of the array is required.
Auxiliary Space: O(N), Since the hashmap requires linear space. 
