import random


class Solution:

    def winner(self):
        return random.randint(1, 3)

    def playerChoice(self):
        return random.randint(1, 3)

    def hostChoice(self, winningChoice, playerChoice):
        hostInitialChoices = [1, 2, 3]
        hostInitialChoices.remove(winningChoice)
        if playerChoice in hostInitialChoices: hostInitialChoices.remove(playerChoice)
        hostChoice = random.choice(hostInitialChoices)
        return hostChoice

    def calculateStrategy(self, s1, s2, s3, N, ans):
        ans[0] = s1 / N
        ans[1] = s2 / N
        ans[2] = s3 / N
        if (ans[0] > ans[1] and ans[0] > ans[2]):
            ans[3] = 1
        elif (ans[1] > ans[0] and ans[1] > ans[2]):
            ans[3] = 2
        else:
            ans[3] = 3
        return ans

    def MontyHall(self, N):
        ans = [0.0, 0.0, 0.0, 0]
        s1 = 0.0
        s2 = 0.0
        s3 = 0.0
        for i in range(N):
            winningChoice = self.winner()
            playerChoice = self.playerChoice()
            hostChoice = self.hostChoice(winningChoice, playerChoice)
            if winningChoice == playerChoice:
                s2 += 1
                s3 += 0.5
            else:
                s1 += 1
                s3 += 0.5
        ans = self.calculateStrategy(s1, s2, s3, N, ans)

        # Write your code here. Please do not change the return statement.
        # Update ans[0], ans[1], ans[2] and ans[3] as mentioned in the question.
        #print(ans)
        return ans


