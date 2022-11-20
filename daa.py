def LCS(A, B, m, n, table):
    if m == 0 or n == 0:
        return ['']
 
    if A[m - 1] == B[n - 1]:
        lcs = LCS(A, B, m - 1, n - 1, table)

        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (A[m - 1])
 
        return lcs
 
   
    if table[m - 1][n] > table[m][n - 1]:
        return LCS(A, B, m - 1, n, table)
 
    
    if table[m][n - 1] > table[m - 1][n]:
        return LCS(A, B, m, n - 1, table)
 
 
    top = LCS(A, B, m - 1, n, table)
    left = LCS(A, B, m, n - 1, table)
 
    return top + left
 
 
def LCSLength(A, B, table):
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
 
 
def findLCS(A, B):
    table = [[0 for x in range(len(B) + 1)] for y in range(len(A) + 1)]
    LCSLength(A, B, table)
    lcs = LCS(A, B, len(A), len(B), table)
    return list(lcs)
 
 

 
A = 'qpqrr'
B = 'pqprqrp'
 
lcs = findLCS(A, B)
print("The length(x) of the longest common subsequence is:")
X = (len(lcs[0]))
print(X)

print("The longest common subsequences are:")    
print(set(lcs))
if X == 0:
  Y = 0
else:
  Y = (len(set(lcs)))

print("There are "+ str(Y) + " longest common subsequences(y).")
print("Then x + 5y is:")
print(X+5*Y)