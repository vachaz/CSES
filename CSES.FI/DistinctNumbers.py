import sys
class Solution:
    def distinctnumbers(self, n, arr):
        return len(set(arr))
if __name__ == '__main__':
    solution = Solution()
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution.distinctnumbers(n,arr))
