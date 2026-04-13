class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        result = 0

        while l<r:
            height = min(heights[l],heights[r])
            width = r - l
            t = height * width
            result = max(result, t)

            if heights[l] >= heights[r]:
                r -=1
            else:
                l += 1


        return result