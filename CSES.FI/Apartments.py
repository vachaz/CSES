class Solution:
    def apartments_solution(self, n, m, k, applicants, apartments):
        apartments.sort()
        applicants.sort()
        i,j, ans = 0, 0, 0
        while i<n and j<m:
            applicant = applicants[i]
            apartment = apartments[j]
            if apartment < applicant - k:
                j+=1
            elif apartment > applicant + k:
                i+=1
            else:
                ans+=1
                i+=1
                j+=1
        return ans
if __name__=='__main__':
    solution = Solution()
    n,m,k = map(int, input().split())
    applicants = list(map(int, input().split()))
    apartments = list(map(int, input().split()))
    print(solution.apartments_solution(n, m, k, applicants, apartments))
