


def product_except_self(nums):
    nums_length = len(nums)
    answer = [1] * nums_length

    for i in range(1, nums_length):
        answer[i] = answer[i - 1] * nums[i - 1]

    right_prod = 1
    for i in range(nums_length - 2, -1, -1):
        right_prod *= nums[i + 1]
        answer[i] = answer[i] * right_prod
    return answer

print([1,2,3,4])
print(product_except_self([1,2,3,4]))
print([-1,1,0,-3,3])
print(product_except_self([-1,1,0,-3,3]))