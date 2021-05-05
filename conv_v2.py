import numpy as np

orig_mat = np.array([[1, 2, 3], [7, 8, 9], [0,0,1]])
filter_mat = np.array([[1,1,1],[0,0,0],[2,10,3]])
conv_mat = np.array([[0,0,0],[0,0,0],[0,0,0]])
res = 0
for i in range(3):
  for j in range(3):
    res = res + (orig_mat[i,j] * filter_mat[i,j])
print(res)