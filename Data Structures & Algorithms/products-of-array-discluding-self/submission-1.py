class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = []
        leng = len(nums)

        left_product = [None] * leng
        left_product[0] = 1
        for i in range(1, leng):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = [None] * leng
        right_product[leng - 1] = 1
        for i in range(leng - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        for i in range(leng):
            product.append(right_product[i] * left_product[i])

        return product