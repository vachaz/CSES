# import sys
# class Solution:
#     def distinctnumbers(self, n, arr):
#         # return len(set(arr))
#         unique_elements = set()
#         for i in arr:
#             unique_elements.add(i)
#         return len(unique_elements)
# if __name__ == '__main__':
#     solution = Solution()
#     n = int(sys.stdin.readline())
#     arr = list(map(int, sys.stdin.readline().split()))
#     print(solution.distinctnumbers(n,arr))
n = int(input())
# create a sorted list of the numbers
numbers = sorted(map(int, input().split()))
ans = 1
for i in range(1, n):
	# if the current number is different from the previous
	# it is a distinct number so we add 1 to the answer
	if numbers[i] != numbers[i - 1]:
		ans += 1
print(ans)