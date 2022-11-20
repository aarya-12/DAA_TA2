# DAA_TA2
# Design-Analysis-and-Algorithms
## Longest common subsequence problem
Consider two strings A = “qpqrr” and B = “pqprqrp”. Let x be the length of the longest common subsequence (not necessarily contiguous) between A and B and let y be the number of such longest common subsequence between A and B. Then find x + 5y.
Write program for above objective with three test cases.

## Approach
There are three main functions : findLCS, LCSLength and LCS.
We give the strings as input to the findLCS() function. It finds all LCS of given strings. Firstly, findLCS() defines table[i][j] which stores the length of LCS of substring 'A[0…i-1]' and 'B[0…j-1]'. Then we call the LCSLength() function to fill up the table. LCSLength() takes the two strings and table as input and fills up the table. We fill the table in a bottom up manner. We use two for loops to iterate the two strings and if the current character matches then we fill the table with incremented diagonal value. If the characters do not match then we choose the maximum of the top or left side values. 
After this the findLCS() function calls the LCS() function which takes the two strings, their lengths and the table as the input. It returns all the LCS strings. If we reach the end of either string, an emtpy list of strings is returned. If the last characters of the two strings match then we ignore the last characters and find all LCS of substring 'A[0…m-2]', 'B[0…n-2]' and store it in a list lcs. Later we append the last character to all the LCS substrings in the list lcs. When the last character of the two strings don't match, we check if a top cell of the current cell has more value than the left cell and then ignore the current character of string A and find all LCS. If a left cell of the current cell has more value than the top cell, then ignore the current character of string B and find all LCS. If the top cell has equal value to the left cell, then we consider both characters and 
merge the two lists and return. findLCS() returns a list of all the lcs we found.

## Language used
Python language was used to write the code.

## Code
```python
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

```
## Example
In this example we've taken two strings A = “qpqrr” and B = “pqprqrp”. If there is a match then table[i][j] = table[i-1][j-1]+1 and if there is no match then table[i][j] = max(table[i-1][j],table[i][j-1]). The following table is generated:
|       | **B** | **p** | **q** | **p** | **r** | **q** | **r** | **p** |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **A** | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| **q** | 0     | 0     | 1     | 1     | 1     | 1     | 1     | 1     |
| **p** | 0     | 1     | 1     | 2     | 2     | 2     | 2     | 2     |
| **q** | 0     | 1     | 1     | 2     | 2     | 3     | 3     | 3     |
| **r** | 0     | 1     | 1     | 2     | 3     | 3     | 4     | 4     |
| **r** | 0     | 1     | 1     | 2     | 3     | 3     | 4     | 4     |

Length of longest common subsequence (LCS) is X = 4. LCS of length 4 are “qprr”, “pqrr” and “qpqr”. Y = 3.
X = 4 and Y = 3
X + 5Y = 19

## Test cases
##### When there are multiple lcs:
<img src="https://github.com/aarya-12/DAA_TA2/blob/a609f2ffbaea3cb2bff07d5d9691726fa52e5be1/case1.png">

##### When there are no lcs:
<img src="https://github.com/aarya-12/DAA_TA2/blob/a609f2ffbaea3cb2bff07d5d9691726fa52e5be1/case2.png">

##### When there is a single lcs:
<img src="https://github.com/aarya-12/DAA_TA2/blob/a609f2ffbaea3cb2bff07d5d9691726fa52e5be1/case3.png">

## How to use?

Enter the input strings. In the output, the length of the longest common subsequence and the number of such lcs are displayed along with X + 5Y.


