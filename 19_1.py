# варіант 20
import numpy as np
import pandas as pd

with open("vector.csv", "r", encoding="cp1251") as f:
    df = pd.read_csv(f, sep=',', encoding="cp1251")

df["Lenght"] = np.sqrt(df['CoordinateX']**2 + df['CoordinateY']**2)
df["Lenght"] = df["Lenght"].apply(lambda x: round(x, 2) if x % 1 != 0 else int(x))
array_data = np.column_stack((df["Vector"].to_numpy(), df["CoordinateX"].to_numpy(), df["CoordinateY"].to_numpy(), df["Lenght"].to_numpy()))

columns = ["Vector", "CoordinateX", "CoordinateY", "Length"]
df1 = pd.DataFrame(array_data, columns=columns)

df1.to_csv("vector_len.csv", sep=",", encoding="cp1251", index=False)
