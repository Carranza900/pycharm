import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt  # gráficos


# cargar datos
file_path = "./Data/Pen Sales Data.xlsx"
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")



# --- Tarea 3: Popularidad de bolígrafos ---
item_sales = pen_sales_df["Item"].value_counts().sort_values(ascending=True)

plt.figure(figsize=(10, 6))
item_sales.plot(kind='barh', color='green', edgecolor='black')
plt.title("Bolígrafos más vendidos")
plt.xlabel("Ventas")
plt.ylabel("Tipo")
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()