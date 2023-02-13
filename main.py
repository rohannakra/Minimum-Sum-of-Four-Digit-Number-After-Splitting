# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

def min_sum(num):
    num_arr = [int(n) for n in str(num)]

    min_1 = min(num_arr)
    num_arr.remove(min_1)

    min_2 = min(num_arr)
    num_arr.remove(min_2)

    return int(str(min_1) + str(num_arr[0])) + int(str(min_2) + str(num_arr[1]))


print(min_sum(2932))
print(min_sum(4009))

# --------------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def minimumSum(self, num: int) -> int:
        num_arr = [int(n) for n in str(num)]

        min_1 = min(num_arr)
        num_arr.remove(min_1)

        min_2 = min(num_arr)
        num_arr.remove(min_2)

        return int(str(min_1) + str(num_arr[0])) + int(str(min_2) + str(num_arr[1]))
