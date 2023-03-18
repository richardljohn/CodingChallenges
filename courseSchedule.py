# LeetCode #207 - Course Schedule

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()

        def dfs(crs):
            if crs in visitSet: 
                return False
            if preMap[crs] == []: 
                return True 
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            return True