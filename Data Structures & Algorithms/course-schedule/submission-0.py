class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dic[crs].append(pre)

        visiting = set()
        print(dic)

        def dfs(c):
            if c in visiting:
                return False

            if dic[c] == []:
                return True
            
            visiting.add(c)
            for pre in dic[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            dic[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True