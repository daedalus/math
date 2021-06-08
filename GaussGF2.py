#!/usr/bin/env python3
# Author Dario Clavijo 2021
# based on https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf, page2

def Gauss_GF2(A):
  h = len(A)
  m = len(A[0])
  marks = [False] * h
  for j in range(0,m):
    for i in range(0,h):
      if A[i][j] == 1:
          marks[i] = True
          for k in range(j+1,m):
            if A[i][k] == 1:
              A[i][k] = (A[i][j] ^ A[i][k]) 
          break
  return marks, A
              
if __name__ == "__main__":
  A  = [[1,1,0,0],[1,1,0,1],[0,1,1,1],[0,0,1,0],[0,0,0,1]]
  marks,A = Gauss_GF2(A)
  print(marks)
  for row in A:
    print(row)

