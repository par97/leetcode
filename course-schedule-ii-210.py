from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp={}  # int -> set(int)
        # 把每个课程 i 的前置条件放到mp[i] 指向的集合中

        for preq in prerequisites:
            course, precourse= preq
            if course in mp:
                mp[course].add(precourse)
            else:
                mp[course]={precourse}

        # 每个课程i 有三个状态
        # 0 代表没有处理过， 1 代表正在处理， 2 代表处理结束
        state=[0]*numCourses 
        ret=[]

        def backtrack(course):
            if state[course]==1:
                # 正在访问，形成环
                return False
            if state[course]==2:
                # 已经访问过
                return True
            
            # 这时state[course]==0:
            # 现在开始处理该数字，置为处理中
            state[course]=1

            # 如果 course 不在mp,说明他没有前置条件。
            if course in mp:
                for preq in mp[course]:
                    if not backtrack(preq):
                        return False
            
            ret.append(course)
            state[course]=2
            return True

        for course in range(numCourses):
            if not backtrack(course):
                return []

        return ret

if __name__=="__main__":
    prerequisites=[[1,0]]
    numCourses=2
    sol=Solution()
    print(sol.findOrder(numCourses,prerequisites))
