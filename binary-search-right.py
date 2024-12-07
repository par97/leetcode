# 查找有重复数字的右边界

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1

        left=0
        right=len(nums)  #左闭右开

        while left < right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid
        # print("left:",left,"right:",right)
        if right==0:
            return -1  
        return right-1 if nums[right-1]==target else -1
    
if __name__=="__main__":
    nums=[0,1,2,3,4,5,5,5,5,5,6,7,8,9]
    sol=Solution()
    print(sol.search(nums,5))
    print(sol.search(nums,3))
    print(sol.search(nums,0))
    print(sol.search(nums,-2))
    print(sol.search(nums,9))
    print(sol.search(nums,10))

    
