import random
import pandas as pd

# Вхідні дані
n = 15
num_objects = 15

# Інтервали критеріїв
k1_min, k1_max = 100*n*0.1, 200*n*0.1   # [150; 300]
k2_min, k2_max = 10*n, 50*n             # [150; 750]
k3_min, k3_max = 0.1*n, 10*n            # [1.5; 150]

# Вагові коефіцієнти
alpha1, alpha2, alpha3 = 0.1, 0.1, 0.8

# 1. Генеруємо дані
objects = []
for i in range(1, num_objects+1):
    k1 = random.randint(int(k1_min), int(k1_max))
    k2 = random.randint(int(k2_min), int(k2_max))
    k3 = round(random.uniform(k3_min, k3_max), 2)
    objects.append((i, k1, k2, k3))

df = pd.DataFrame(objects, columns=["No", "k1", "k2", "k3"])
print("\n=== Згенеровані дані ===")
print(df)

# 2. Формуємо множину Парето
pareto = []
for i, obj in df.iterrows():
    dominated = False
    for j, other in df.iterrows():
        if (other["k1"] >= obj["k1"] and
            other["k2"] <= obj["k2"] and
            other["k3"] >= obj["k3"] and
            (other["k1"] > obj["k1"] or other["k2"] < obj["k2"] or other["k3"] > obj["k3"])):
            dominated = True
            break
    if not dominated:
        pareto.append(obj)

pareto_df = pd.DataFrame(pareto)
print("\n=== Множина Парето ===")
print(pareto_df)

# 3. З урахуванням вагових коефіцієнтів
pareto_df["k1w"] = pareto_df["k1"] * alpha1
pareto_df["k2w"] = pareto_df["k2"] * alpha2
pareto_df["k3w"] = pareto_df["k3"] * alpha3

# 4. Нормування
pareto_df["k1n"] = pareto_df["k1w"] / pareto_df["k1w"].max()
pareto_df["k2n"] = pareto_df["k2w"] / pareto_df["k2w"].max()
pareto_df["k3n"] = pareto_df["k3w"] / pareto_df["k3w"].max()

# 5. Функція корисності (k1 і k3 додаємо, k2 віднімаємо)
pareto_df["F"] = pareto_df["k1n"] - pareto_df["k2n"] + pareto_df["k3n"]

print("\n=== Нормовані значення з функцією корисності ===")
print(pareto_df[["No","k1n","k2n","k3n","F"]])

# 6. Оптимальне рішення
best = pareto_df.loc[pareto_df["F"].idxmax()]
print("\n=== Оптимальне рішення ===")
print(best)