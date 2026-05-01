class Solution:
    def ferrisWheel(self, n, x, weights):
        weights.sort()
        i, j, ans = 0, n-1, 0
        while i<=j:
            if weights[i] + weights[j] <= x:
                i += 1
            j -= 1
            ans += 1
        return ans

if __name__ == "__main__":
    n, x = map(int, input().split())
    weights = list(map(int, input().split()))
    solution = Solution()
    print(solution.ferrisWheel(n, x, weights))