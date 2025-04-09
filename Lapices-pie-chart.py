import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
file_path = r"Pen Sales Data.xlsx"
xls = pd.ExcelFile(file_path)

# Carga los datos de la hoja principal
pen_sales_df = pd.read_excel(xls, sheet_name="Pen Sales")

# Convierte la columna de fecha de compra a formato de fecha y hora
pen_sales_df["Purchase Date"] = pd.to_datetime(pen_sales_df["Purchase Date"])

# Creo una columna con el mes y año para agrupar las ventas
pen_sales_df["Year-Month"] = pen_sales_df["Purchase Date"].dt.to_period("M")

# Cuenta el número de ventas por mes
monthly_sales = pen_sales_df.groupby("Year-Month").size()

# Graficá las ventas a lo largo del tiempo
plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', linestyle='-', color='b')
plt.title("Tendencias de ventas a lo largo del tiempo (por mes)", fontsize=14)
plt.xlabel("Fecha (Año-Mes)", fontsize=12)
plt.ylabel("Número de Ventas", fontsize=12)
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
