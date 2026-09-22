class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arr = [(value, index) for index, value in enumerate(nums)]

        arr.sort()

        i = 0
        j = len(arr) - 1

        while i < j:
            if arr[i][0] + arr[j][0] == target:
                return [arr[i][1], arr[j][1]]

            elif arr[i][0] + arr[j][0] > target:
                j -= 1

            else:
                i += 1

        return target, "not found"