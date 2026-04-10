class Solution:
    def weirdAlgorithm(self, n):
        print(n, end=" ")
        while(n!=1):
            if n%2 == 0:
                n=int(n/2)
            else:
                n=int(3*n+1)
            if n != None:
                print(n, end=" ")
        return
if __name__ == '__main__':
        solution = Solution()
        n = int(input())
        solution.weirdAlgorithm(n)

