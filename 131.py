from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)

        ret=[]
        temp=[]

        def isPal(s):
            return s==s[::-1]

        def backtrack(i):
            print("temp", temp)
            print("i", i)
            if i==n:
                return
            for j in range(i+1, n):
                substring=s[i:j]
                print(i,j, substring)
                if isPal(substring):
                    print("ispal:", substring)
                    temp.append(substring)
                    backtrack(j)
                    temp.pop()
                else:
                    print("not pal:", substring)

        backtrack(0)

s = Solution()
s.partition("aab")