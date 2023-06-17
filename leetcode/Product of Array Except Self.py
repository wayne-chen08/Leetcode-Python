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
