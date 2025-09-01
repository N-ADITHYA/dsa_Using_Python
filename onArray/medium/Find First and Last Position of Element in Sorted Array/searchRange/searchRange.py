from typing import List

class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def firstO(arr, tar):
            left, right = 0, len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == tar:
                    ans = mid
                    right = mid - 1
                elif arr[mid] > tar:
                    right = mid - 1
                elif arr[mid] < tar:
                    left = mid + 1
            return ans

        def sec0(arr, tar):
            left, right = 0, len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == tar:
                    ans = mid
                    left = mid + 1
                elif arr[mid] > tar:
                    right = mid - 1
                elif arr[mid] < tar:
                    left = mid + 1
            return ans

        return [firstO(arr, target), sec0(arr, target)]

if __name__ == "__main__":
    sl = Solution()
    print(sl.searchRange([1,2,3,3,3,3,3], 3))

