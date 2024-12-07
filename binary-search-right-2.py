# 查找有重复数字的右边界

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1

        left=0
        right=len(nums)-1  #左闭右闭

        while left <= right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        # print("left:",left,"right:",right)

        if right<0 or nums[right]!=target:
            return -1
        else:
            return right
    
if __name__=="__main__":
    nums=[0,1,2,3,4,5,5,5,5,5,6,7,8,9]
    sol=Solution()
    print(sol.search(nums,5))
    print(sol.search(nums,3))
    print(sol.search(nums,0))
    print(sol.search(nums,-2))
    print(sol.search(nums,9))
    print(sol.search(nums,10))

    
