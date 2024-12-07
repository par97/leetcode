from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={}  # int -> set(int)
        # 把每个课程 i 的前置条件放到mp[i] 指向的集合中
        for l in prerequisites:
            course, preq=l
            if course in mp:
                mp[course].add(preq)
            else:
                mp[course]={preq}     

        # 每个课程i 有三个状态
        # 0 代表没有处理过， 1 代表正在处理， 2 代表处理结束
        state=[0]*numCourses  

        def backtrace(i)-> bool:
            # 已经处理过了，直接跳过
            if state[i]==2:
                return True

            # 遇到了一个正在处理的节点，形成了环
            if state[i]==1:
                return False
            
            # 这时state[i]==0:
            # 现在开始处理该数字，置为处理中
            state[i]=1
            
            # i 不在mp,说明他没有前置条件。
            if i in mp:
                preqs=mp[i]
                for preq in preqs:
                    if not backtrace(preq):
                        return False
            
            #已经处理完该数字，置为处理结束
            state[i]=2
            return True

        for i in range(numCourses):
            if not backtrace(i):
                return False

        return True   
    
if __name__=="__main__":
    prerequisites=[[1,0]]
    numCourses=2
    sol=Solution()
    print(sol.canFinish(numCourses,prerequisites))