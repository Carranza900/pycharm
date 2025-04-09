import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
file_path = r"Pen Sales Data.xlsx"
xls = pd.ExcelFile(file_path)

# Carga los datos de la hoja principal
pen_sales_df = pd.read_excel(xls, sheet_name="Pen Sales")

# --- Tarea 1: Rendimiento de las ventas a lo largo del tiempo ---
# Convertir la columna de fecha de compra a formato de fecha y hora
pen_sales_df["Purchase Date"] = pd.to_datetime(pen_sales_df["Purchase Date"])

# Crear una columna con el mes y año para agrupar las ventas
pen_sales_df["Year-Month"] = pen_sales_df["Purchase Date"].dt.to_period("M")

# Contar el número de ventas por mes
monthly_sales = pen_sales_df.groupby("Year-Month").size()

# Graficar las tendencias de ventas a lo largo del tiempo
plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', linestyle='-', color='b')
plt.title("Tendencias de ventas a lo largo del tiempo (por mes)", fontsize=14)
plt.xlabel("Fecha (Año-Mes)", fontsize=12)
plt.ylabel("Número de Ventas", fontsize=12)
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Tarea 2: Análisis de costos de envío ---
# Limpiar y convertir la columna de "Shipping Cost" a formato numérico
pen_sales_df["Shipping Cost"] = (
    pen_sales_df["Shipping Cost"]
    .str.replace(r'[^\d.\-]', '', regex=True)
    .replace('-', '0')  # Reemplazar valores "-" por "0"
    .replace('', '0')  # Reemplazar cadenas vacías por "0"
    .astype(float)  # Convertir a número flotante
)

# Calcular la distribución del costo de envío
shipping_cost_distribution = pen_sales_df["Shipping Cost"].describe()

# Agrupar por artículo y calcular el costo promedio de envío
average_shipping_cost = pen_sales_df.groupby("Item")["Shipping Cost"].mean().sort_values()

# Mostrar la distribución en consola
print("Distribución del costo de envío:")
print(shipping_cost_distribution)

# Graficar el costo promedio de envío por tipo de bolígrafo (barras horizontales y color morado)
plt.figure(figsize=(10, 6))
average_shipping_cost.plot(kind='barh', color='purple', edgecolor='black')
plt.title("Costo Promedio de Envío por Tipo de Bolígrafo", fontsize=14)
plt.xlabel("Costo Promedio de Envío", fontsize=12)
plt.ylabel("Tipo de Bolígrafo", fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
