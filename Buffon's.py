


import math
import random


class Solution:
    def __init__(self):
        pass

    def Simulate(self, l, N):
        ans = [0 for i in range(math.floor(l) + 2)]
        for i in range( N):
            top = random.uniform(0, 1)
            a = random.uniform(0, math.pi)
            height = l * math.sin(a)
            lines = math.floor((height + top))
            if top == 0:
                lines = lines + 1
            ans[lines] = ans[lines] + 1
        for i in range(len(ans)):
            ans[i] = ans[i] /N

        # Write your code here. Please do not change the return statement.
        # Accurately compute the number of possible values X can take. Say it is m.
        # Return an array containing floating point numbers (keep its name: ans) with m entries such that P(X = i) = ans[i]
        # Do not forget that indexing starts at 0.

        return ans


