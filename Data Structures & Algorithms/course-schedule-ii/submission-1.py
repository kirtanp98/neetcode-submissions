class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dic[crs].append(pre)

        visiting, checked = set(), set()
        result = []

        def dfs(c):
            if c in visiting:
                return False

            if c in checked:
                return True

            visiting.add(c)
            for pre in dic[c]:
                if not dfs(pre):
                    return False
            
            visiting.remove(c)
            checked.add(c)
            result.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result