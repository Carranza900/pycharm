import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt


# cargar datos
file_path = "../Data/Pen Sales Data.xlsx"
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")


# --- Tarea 2: Costo de envío promedio ---
pen_sales_df["Shipping Cost"] = (
    pen_sales_df["Shipping Cost"]
    .fillna("0")
    .astype(str)
    .str.replace(r'[^\d.\-]', '', regex=True)
    .replace({'-': '0', '': '0'})
    .astype(float)
)
avg_shipping = pen_sales_df.groupby("Item")["Shipping Cost"].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_shipping.plot(kind="barh", color="purple")
plt.title("Costo envío promedio")
plt.xlabel("Costo medio")
plt.ylabel("Artículo")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()