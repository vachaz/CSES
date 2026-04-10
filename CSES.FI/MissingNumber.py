class Solution:
    def missingNumber(self, n, arr):
        xor = 0
        for i in range(1, n + 1):
            xor ^= i
        for num in arr:
            xor ^= num
        return xor
if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution.missingNumber(n, arr))