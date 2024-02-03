"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]"""

#program

class Solution(object):
    def productExceptSelf(self, nums):
       
        n = len(nums)

        left_products = [1] * n
        right_products = [1] * n
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product

        
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

       
        output = [left_products[i] * right_products[i] for i in range(n)]

        return output

  """output
  Input
nums =
[1,2,3,4]
Output
[24,12,8,6]"""
