class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0]*len(nums)

        for i,x in enumerate(nums):
            if i == 0:
                prefix.append(x)
            else:
                prefix.append(x*prefix[i-1])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i]*postfix[i+1]


        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(1*postfix[i+1])
            elif i == len(nums)-1:
                result.append(prefix[i-1]*1)
            else:
                result.append(prefix[i-1]*postfix[i+1])

        return result