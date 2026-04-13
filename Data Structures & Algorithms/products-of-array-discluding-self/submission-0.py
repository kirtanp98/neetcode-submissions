from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = reduce(lambda x, y: x * y if y != 0 else x, nums)
        haszero = nums.count(0)
        result = [] 

        for x in nums:
            print(nums)
            if x == 0 and haszero == 1:
                result.append(product)
            elif haszero >= 1:
                result.append(0)
            else:
                result.append(product // x)

        return result
