# 子集
class Solution:
	def subsets(self, nums):		
                if not nums:
			return []
		res = []
		n = len(nums)

		def helper(idx, temp_list):
			res.append(temp_list)
			for i in range(idx, n):
				helper(i + 1, temp_list + [nums[i]])

		helper(0, [])
		return res
    
    
 # 全排列  回溯算法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return 
        
        res = []
        n = len(nums)
        f = [0]*n    # 0代表没有走过
        
        def helper(tmp,len,f):
            if len == n:
                res.append(tmp)
                return
            for i in range(n):
                if f[i]:
                    continue
                f[i] = 1
                helper(tmp + [nums[i]], len+1, f)
                f[i] = 0
                
        helper([],0,f)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return 
        
        res = []
        n = len(nums)
        
        def helper(nums,tmp,length):
            if length == n:
                res.append(tmp)
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], tmp + [nums[i]], length+1)
                
        helper(nums,[],0)
        
        return res
        
   
