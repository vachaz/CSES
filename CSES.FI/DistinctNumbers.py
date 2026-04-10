import sys
class Solution:
    def distinctnumbers(self, n, arr):
        # return len(set(arr))
        unique_elements = set()
        for i in arr:
            unique_elements.add(i)
        return len(unique_elements)
if __name__ == '__main__':
    solution = Solution()
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution.distinctnumbers(n,arr))
