#Backtracking: N-Queens
n=4
ans=[]
board=[[0]*n for _ in range(n)]
#print(board)

def isSafe(board,i,j):
    for k in range(j):                #check condition for row
        if board[i][k]==1:
            return False
    for k in range(i):                  #check condition for column
        if board[k][j]==1:
            return False
    row=i
    col=j 
    while (row>=0 and col>=0):
        if board[row][col]==1:
            return False
        row=row-1
        col=col-1    
    while (i<n and j>=0):
        if board[i][j]==1:
            return False
        i=i+1
        j=j-1    
    return True        

def saveSol(board,ans):
    temp=[]
    for i in range(n):
        for j in range(n):
            temp.append(board[i][j])
    ans.append(temp)

            
    #for and in 2-d array (only single line)       

def solve(board,ans,n,j):
    if j==n:
        saveSol(board,ans)
        return 
    for i in range(n):
        if isSafe(board,i,j):
            board[i][j]=1
            solve(board,ans,n,j+1)
            board[i][j]=0

def display():
    for i in range(len(ans)):
        print(ans[i],end=" ")
        print("\n")    

solve(board,ans,n,0)
display()