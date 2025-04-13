import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt  # gráficos
import string  # para limpiar texto

# cargar datos
file_path = "./Data/Pen Sales Data.xlsx"
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")


# --- Tarea 4: Tiempo medio de entrega ---
pen_sales_df["Delivery Date"] = pd.to_datetime(pen_sales_df["Delivery Date"])
pen_sales_df["Delivery Time"] = (pen_sales_df["Delivery Date"] - pen_sales_df["Purchase Date"]).dt.days
avg_delivery = pen_sales_df.groupby("Item")["Delivery Time"].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_delivery.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Tiempo medio de entrega")
plt.xlabel("Artículo")
plt.ylabel("Días")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()