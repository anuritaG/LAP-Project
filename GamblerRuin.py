import random
class Solution:
    def __init__(self):
        pass


    def Simulate(self, p, i, N):
        ans = [0.0, 0.0, 0.0, 0.0, 0.0]
        numberWinS1 = 0
        numberWinS2=0
        numberBetS1 = 0
        numberBetS2 = 0
    	# Write your code here. Please do not change the return statement.
        # Update ans[0], ans[1], ans[2] and ans[3] as mentioned in the question.
        for j in range(1,N+1):
            initialMoneyS1=i
            initialMoneyS2=i
            while (initialMoneyS1 != 0 and initialMoneyS1 != 2 * i):
                numberBetS1 += 1
                probability = random.uniform(0, 1)
                if probability <= p:
                    initialMoneyS1 += i
                else:
                    initialMoneyS1 -= i
            while(initialMoneyS2!=0 and initialMoneyS2!=2*i):
                probability=random.uniform(0,1)
                numberBetS2+=1
                if probability<= p:
                  initialMoneyS2+=1
                else:
                    initialMoneyS2-=1
            if initialMoneyS1==2*i:
                numberWinS1+=1
            if initialMoneyS2==2*i:
                numberWinS2+=1
        ans[0]= numberWinS1/N
        ans[1]= numberWinS2/N
        ans[2]= numberBetS1/N
        ans[3]=numberBetS2/N
        if ans[0]>ans[1]:
            ans[4]=1
        else:
            ans[4]=2
        return ans



