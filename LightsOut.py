class Solution:
    def __init__(self):
        pass

    def LightsOut(self, N, s):
        ans = [0 for i in range(N**2+1)]
    	# Write your code here. Please do not change the return statement.
        # Do not forget that indexing starts at 0.
        rows, cols = (N*N, N*N)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        count = 0
        for i in range(0,N):
            for j in range(0,N):
                arr[i*N+j][count]=1
                if (i+1)<N:
                    arr[(i+1)*N+j][count]=1
                if (j+1)<N:
                    arr[(i)*N+j+1][count]=1
                if (j-1)>=0:
                    arr[(i)*N+j-1][count]=1
                if (i-1)>=0:
                    arr[(i-1)*N+j][count]=1
                count=count+1
        for i in range(0,N*N):
            if arr[i][i] != 1:
                for j in range(i, N * N):
                    if arr[j][i] == 1:
                        for k in range(N * N):
                            temp = arr[i][k]
                            arr[i][k] = arr[j][k]
                            arr[j][k] = temp
                        temp = s[i]
                        s[i] = s[j]
                        s[j] = temp
                        break
            ccol=i
            for k in range(0,N*N):
                if k!= i and arr[k][ccol]==1:
                    for z in range(N*N):
                        arr[k][z]=(arr[k][z]+arr[i][z])%2
                    s[k]=(s[k]+s[i])%2
        flag=0
        for i in range(N * N):
            if arr[i][i]==s[i]:
                ans[i+1]=s[i]
            elif arr[i][i]==1 and s[i]==0:
                ans[i+1]=0
            else:
                flag=1
                break
        if flag==0:
            ans[0]=1
        else:
            for i in range(N*N):
                ans[i]=0
        return ans

t= Solution()
ans=t.LightsOut(  5,  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1])
print(ans)