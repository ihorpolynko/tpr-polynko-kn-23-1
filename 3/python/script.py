import numpy as np
import pandas as pd

matrices = [
    # A1
    [[0,0,1,1,1],
     [1,0,1,1,1],
     [0,0,0,1,1],
     [0,0,0,0,1],
     [0,0,0,0,0]],

    # A2
    [[0,1,0,1,1],
     [0,0,1,1,1],
     [1,0,0,1,1],
     [0,0,0,0,1],
     [0,0,0,0,0]],

    # A3
    [[0,1,1,0,1],
     [0,0,1,1,1],
     [0,0,0,1,1],
     [1,0,0,0,1],
     [0,0,0,0,0]],

    # A4
    [[0,1,1,1,0],
     [0,0,1,1,1],
     [0,0,0,1,1],
     [0,0,0,0,1],
     [1,0,0,0,0]],

    # A5
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,0,0,1,1],
     [0,0,0,0,1],
     [0,0,0,1,0]],

    # A6
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,0,1,1,0],
     [0,0,0,0,1],
     [0,0,1,0,0]],

    # A7
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,0,0,1,0],
     [0,0,1,0,1],
     [0,0,0,0,0]],

    # A8
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,0,1,0,1],
     [0,1,0,0,0],
     [0,0,0,0,0]],

    # A9
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,0,0,1,1],
     [0,0,0,0,1],
     [0,1,0,0,0]],

    # A10
    [[0,1,1,1,1],
     [0,0,1,1,1],
     [0,1,0,1,1],
     [0,0,0,0,1],
     [0,0,0,0,0]]
]

names = [f"A{i+1}" for i in range(len(matrices))]

# --- Обчислення відстаней Кемені ---
n = len(matrices)
dist_matrix = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = np.sum(np.abs(np.array(matrices[i]) - np.array(matrices[j])))

# --- Знаходження медіани Кемені ---
sum_distances = np.sum(dist_matrix, axis=1)
min_dist = np.min(sum_distances)
median_indices = np.where(sum_distances == min_dist)[0]
median_names = [names[i] for i in median_indices]

# --- Знаходження середнього за Кемені ---
sum_squared = np.sum(dist_matrix**2, axis=1)
min_sq = np.min(sum_squared)
mean_indices = np.where(sum_squared == min_sq)[0]
mean_names = [names[i] for i in mean_indices]

# --- Вивід результатів ---
print("Матриця попарних відстаней Кемені:")
print(pd.DataFrame(dist_matrix, index=names, columns=names))
print("\nСума відстаней для кожного експерта:")
for i, s in enumerate(sum_distances):
    print(f"{names[i]}: {s}")

print(f"\nМінімум суми відстаней (Медіана Кемені) = {min_dist}")
print(f"Медіана Кемені (експерт/и): {median_names}")

print(f"\nМінімум суми квадратів відстаней (Середнє за Кемені) = {min_sq}")
print(f"Середнє за Кемені (експерт/и): {mean_names}")
