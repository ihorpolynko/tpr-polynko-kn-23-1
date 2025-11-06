import numpy as np

# --- Дані ---
alternatives = ["Раківка", "Центр", "Молодіжне"]
criteria = ["Вартість", "Площа", "Час до роботи"]

criteria_matrix = np.array([
    [1,   3,   5],
    [1/3, 1,   2],
    [1/5, 1/2, 1]
])

K1 = np.array([
    [1,   5,   3],
    [1/5, 1,   1/4],
    [1/3, 4,   1]
])

K2 = np.array([
    [1,   3,   1/2],
    [1/3, 1,   1/5],
    [2,   5,   1]
])

K3 = np.array([
    [1,   1/5, 1/3],
    [5,   1,   3],
    [3,   1/3, 1]
])

# --- Функція AHP ---
def ahp(matrix):
    eigvals, eigvecs = np.linalg.eig(matrix)
    max_index = np.argmax(eigvals.real)
    max_eigval = eigvals.real[max_index]
    weights = eigvecs[:, max_index].real
    weights /= np.sum(weights)
    CI = (max_eigval - len(matrix)) / (len(matrix) - 1)
    RI = {1:0, 2:0, 3:0.58, 4:0.9, 5:1.12}.get(len(matrix), 1.24)
    CR = CI / RI
    return weights, CR

# --- Розрахунки ---
wK1, cr1 = ahp(K1)
wK2, cr2 = ahp(K2)
wK3, cr3 = ahp(K3)
wc, crc = ahp(criteria_matrix)

local_matrix = np.array([wK1, wK2, wK3]).T
global_priorities = np.dot(local_matrix, wc)

# --- Вивід ---
print("=== Вектори пріоритетів по критеріях ===")
for i, alt in enumerate(alternatives):
    print(f"{alt}: {np.round(local_matrix[i], 4)}")

print("\n=== Вага критеріїв ===")
for c, w in zip(criteria, np.round(wc, 4)):
    print(f"{c}: {w}")

print("\n=== Глобальні пріоритети ===")
ranking = sorted(zip(alternatives, global_priorities), key=lambda x: x[1], reverse=True)
for i, (alt, val) in enumerate(ranking, 1):
    print(f"{i}. {alt} — {val:.4f}")

print("\nCR критеріїв:", round(crc, 4))
print("CR вартості:", round(cr1, 4))
print("CR площі:", round(cr2, 4))
print("CR часу:", round(cr3, 4))