# -*- coding: utf-8 -*-
"""fem gst assembly i guess its correct code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhqM1_Qki8FHhK6Eep5joxO40n9be87r
"""

import numpy as np
import pandas as pd

def generate_indices_csv(n, num_rows):
    indices = np.random.randint(1, n+1, size=(num_rows, n))
    indices_df = pd.DataFrame(indices)
    indices_df.to_csv('indices.csv', index=False, header=False)

n = 4
num_rows = 14
generate_indices_csv(n, num_rows)

import numpy as np
import pandas as pd

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

def generate_indices_csv(n, num_rows):
    indices = np.random.randint(1, n+1, size=(num_rows, n))
    indices_df = pd.DataFrame(indices)
    indices_df.to_csv('indices.csv', index=False, header=False)

def generate_element_stiffness_matrices(n):
    element_stiffness_matrices = [np.random.randint(1, 10, size=(n, n)) for i in range(n)]
    return element_stiffness_matrices

global_stiffness_matrix_order = 10
num_rows = 4
generate_indices_csv(global_stiffness_matrix_order, num_rows)
indices_df = pd.read_csv('indices.csv')
element_stiffness_matrices = generate_element_stiffness_matrices(global_stiffness_matrix_order)
global_stiffness_matrix = assemble_global_stiffness_matrix(global_stiffness_matrix_order, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)

import numpy as np
import pandas as pd

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

n = 10
element_stiffness_matrices = [np.array([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]),
                             np.array([[5, 6, 7, 8], [6, 7, 8, 5], [7, 8, 5, 6], [8, 5, 6, 7]]),
                             np.array([[9, 10, 11, 12], [10, 11, 12, 9], [11, 12, 9, 10], [12, 9, 10, 11]]),
                             np.array([[13, 14, 15, 16], [14, 15, 16, 13], [15, 16, 13, 14], [16, 13, 14, 15]])]
indices_df = pd.read_csv('indices.csv')
global_stiffness_matrix = assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)

import numpy as np
import pandas as pd

def generate_indices_csv(filename, n, num_element_stiffness_matrices):
    indices = np.zeros((num_element_stiffness_matrices, 4), dtype=int)
    for i in range(num_element_stiffness_matrices):
        indices[i, :] = np.random.randint(1, n+1, 4)
    df = pd.DataFrame(indices, columns=['i1', 'i2', 'i3', 'i4'])
    df.to_csv(filename, index=False)

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                if index[row] <= n and index[col] <= n:
                    global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

n = 14
num_element_stiffness_matrices = 4
element_stiffness_matrices = [np.array([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]),
                             np.array([[5, 6, 7, 8], [6, 7, 8, 5], [7, 8, 5, 6], [8, 5, 6, 7]]),np.array([[5, 6, 7, 8], [6, 7, 8, 5], [7, 8, 5, 6], [8, 5, 6, 7]]),np.array([[5, 6, 7, 8], [6, 7, 8, 5], [7, 8, 5, 6], [8, 5, 6, 7]])]
filename = 'indices.csv'
generate_indices_csv(filename, n, num_element_stiffness_matrices)
indices_df = pd.read_csv(filename)
global_stiffness_matrix = assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)
# Plot the global stiffness matrix as a sparse plot array
plt.spy(global_stiffness_matrix, markersize=15, color='black')
plt.show()
# Save the global stiffness matrix in a text file
np.savetxt("global_stiffness_matrix.txt", global_stiffness_matrix, fmt='%d')

import numpy as np
import pandas as pd

def generate_indices_csv(filename, n, num_element_stiffness_matrices):
    indices = np.zeros((num_element_stiffness_matrices, 5), dtype=int)
    for i in range(num_element_stiffness_matrices):
        indices[i, :] = np.random.randint(1, n+1, 5)
    df = pd.DataFrame(indices, columns=['i1', 'i2', 'i3', 'i4', 'i5'])
    df.to_csv(filename, index=False)

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                if index[row] <= n and index[col] <= n:
                    global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

n = 140
num_element_stiffness_matrices = 1
element_stiffness_matrices = [np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]),
                             np.array([[5, 6, 7, 8, 9], [6, 7, 8, 9, 5], [7, 8, 9, 5, 6], [8, 9, 5, 6, 7], [9, 5, 6, 7, 8]])]
filename = 'indices.csv'
generate_indices_csv(filename, n, num_element_stiffness_matrices)
indices_df = pd.read_csv(filename)
global_stiffness_matrix = assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)
# Plot the global stiffness matrix as a sparse plot array
plt.spy(global_stiffness_matrix, markersize=15, color='black')
plt.show()

import numpy as np
import pandas as pd

def generate_indices_csv(filename, n, num_element_stiffness_matrices):
    indices = np.zeros((num_element_stiffness_matrices, 2), dtype=int)
    for i in range(num_element_stiffness_matrices):
        indices[i, :] = np.random.randint(1, n+1, 2)
    df = pd.DataFrame(indices, columns=['i1', 'i2'])
    df.to_csv(filename, index=False)

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                if index[row] <= n and index[col] <= n:
                    global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

n = 2
num_element_stiffness_matrices = 1
element_stiffness_matrices = [np.array([[1, 2], [2, 1]])]
filename = 'indices.csv'
generate_indices_csv(filename, n, num_element_stiffness_matrices)
indices_df = pd.read_csv(filename)
global_stiffness_matrix = assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)
# Plot the global stiffness matrix as a sparse plot array
plt.spy(global_stiffness_matrix, markersize=15, color='black')
plt.show()

import numpy as np
import pandas as pd

def generate_indices_csv(filename, n, num_element_stiffness_matrices):
    indices = np.zeros((num_element_stiffness_matrices, 6), dtype=int)
    for i in range(num_element_stiffness_matrices):
        indices[i, :] = np.random.randint(1, n+1, 6)
    df = pd.DataFrame(indices, columns=['i1', 'i2', 'i3', 'i4', 'i5','i6'])
    df.to_csv(filename, index=False)

def assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df):
    global_stiffness_matrix = np.zeros((n, n))
    for i, row in indices_df.iterrows():
        index = row.tolist()
        for row in range(element_stiffness_matrices[i].shape[0]):
            for col in range(element_stiffness_matrices[i].shape[1]):
                if index[row] <= n and index[col] <= n:
                    global_stiffness_matrix[index[row]-1, index[col]-1] += element_stiffness_matrices[i][row, col]
    return global_stiffness_matrix

n = 14
num_element_stiffness_matrices = 1
element_stiffness_matrices = [np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2], [4, 5, 1, 2, 3], [5, 1, 2, 3, 4],[5, 1, 2, 3, 4]])]
filename = 'indices.csv'
generate_indices_csv(filename, n, num_element_stiffness_matrices)
indices_df = pd.read_csv(filename)
global_stiffness_matrix = assemble_global_stiffness_matrix(n, element_stiffness_matrices, indices_df)
print(global_stiffness_matrix)