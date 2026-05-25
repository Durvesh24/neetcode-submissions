class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
        
        for i in range(len(nums)):
            mul = 1 
            for j in range(len(nums)):
                if i!= j :
                    mul*=nums[j]

            pro.append(mul)
        return pro 
                

