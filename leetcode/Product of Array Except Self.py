'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
nums = [1,2,3,4]

def productExceptSelf(nums):
    
    answer, suf,pre = [1] * len(nums), 1, 1 #從後面開始乘和從前面開始乘
    for i in range(len(nums)):
        answer[i] *= pre
        pre *= nums[i]
        answer[-1-i] *= suf
        suf *= nums[-1-i]
    return answer

print(productExceptSelf(nums))
