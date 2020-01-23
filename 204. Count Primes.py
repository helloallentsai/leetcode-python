from math import sqrt, ceil


class Solution:
    def countPrimes(self, n: int) -> int:
        n = n-1
        count = 0
        while n > 1:
            if self.checkPrime(n) == True:
                count += 1
            n -= 1
        return count

    def checkPrime(self, n):
        if n == 2:
            return True
        else:
            for num in range(ceil(sqrt(n)), 1, -1):
                if n % num == 0:
                    return False
            return True


test = Solution()
# print(test.checkPrime(13))
# print(test.checkPrime(14))
# print(test.checkPrime(15))
print(test.countPrimes(499979))

# needs to optomize
