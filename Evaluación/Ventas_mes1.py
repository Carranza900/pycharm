import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt


# cargar datos
file_path = "../Data/Pen Sales Data.xlsx"
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")


# --- Tarea 1: Ventas por mes ---
pen_sales_df["Purchase Date"] = pd.to_datetime(pen_sales_df["Purchase Date"])
pen_sales_df["Year-Month"] = pen_sales_df["Purchase Date"].dt.to_period("M")
monthly_sales = pen_sales_df.groupby("Year-Month").size()

plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', linestyle='-', color='b')
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad de ventas")
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()