import numpy as np
from scipy.optimize import linprog

# 1. Початкова платіжна матриця (варіант 15)
A = np.array([
    [-1, -4,  5,  3],
    [ 7,  7,  4, -2],
    [ 5,  4, -3,  6],
    [ 0, -4,  6,  5]
], dtype=float)

print("Початкова матриця:")
print(A)

# --- 1. Спрощення матриці (видалення домінованих рядків та стовпців) ---
def remove_dominated_rows(matrix):
    rows_to_keep = []
    for i in range(len(matrix)):
        dominated = False
        for j in range(len(matrix)):
            if i != j and all(matrix[j] >= matrix[i]) and any(matrix[j] > matrix[i]):
                dominated = True
                break
        if not dominated:
            rows_to_keep.append(i)
    return matrix[rows_to_keep, :]

def remove_dominated_cols(matrix):
    matrix_t = matrix.T
    cols_to_keep = []
    for i in range(len(matrix_t)):
        dominated = False
        for j in range(len(matrix_t)):
            if i != j and all(matrix_t[j] <= matrix_t[i]) and any(matrix_t[j] < matrix_t[i]):
                dominated = True
                break
        if not dominated:
            cols_to_keep.append(i)
    return matrix[:, cols_to_keep]

A_simple = remove_dominated_rows(A)
A_simple = remove_dominated_cols(A_simple)
print("\nСпрощена матриця:")
print(A_simple)

# --- 2. Знаходження сідлової точки ---
row_min = A_simple.min(axis=1)
col_max = A_simple.max(axis=0)
maximin = row_min.max()
minimax = col_max.min()

row_index = np.where(row_min == maximin)[0]
col_index = np.where(col_max == minimax)[0]

saddle_points = [(i,j) for i in row_index for j in col_index if A_simple[i,j] == maximin]

if saddle_points:
    print("\nСідлова точка:", saddle_points)
    print("Ціна гри:", maximin)
