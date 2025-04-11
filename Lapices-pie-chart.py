import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta del archivo Excel
file_path = "./Data/Pen Sales Data.xlsx"

# Verificar si el archivo existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo no se encontró en la ruta especificada: {file_path}")

# Cargar los datos de la hoja principal
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")

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
    .fillna("0")  # Reemplaza valores nulos
    .astype(str)  # Convertir todo a string antes de usar .str
    .str.replace(r'[^\d.\-]', '', regex=True)
    .replace({'-': '0', '': '0'})  # Reemplazar guiones o vacíos por 0
    .astype(float)  # Convertir a número flotante
)

# Agrupar por artículo y calcular el costo promedio de envío
df_avg_pen_cost = pen_sales_df.groupby("Item")["Shipping Cost"].mean().sort_values()

# Graficar el costo promedio de envío en forma horizontal
plt.figure(figsize=(10, 6))
df_avg_pen_cost.plot(kind="barh", color="purple")
plt.title("Costo de envío promedio por producto", fontsize=14)
plt.xlabel("Costo Medio de Envío", fontsize=12)
plt.ylabel("Tipo de Producto", fontsize=12)
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# --- Tarea 3: Ranking de popularidad de bolígrafos ---
item_sales = pen_sales_df["Item"].value_counts()

# Ordena en orden descendente
item_sales_sorted = item_sales.sort_values(ascending=True)

# Grafica el ranking de popularidad
plt.figure(figsize=(10, 6))
item_sales_sorted.plot(kind='barh', color='green', edgecolor='black')
plt.title("Top-Selling Pens", fontsize=14)
plt.xlabel("Number of Sales", fontsize=12)
plt.ylabel("Pen Type", fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

# --- Tarea 4: Análisis de Tiempo de Entrega ---
# Convertir las columnas de fecha de compra y fecha de entrega a formato de fecha
pen_sales_df["Delivery Date"] = pd.to_datetime(pen_sales_df["Delivery Date"])

# Calcular el tiempo de entrega en días
pen_sales_df["Delivery Time"] = (pen_sales_df["Delivery Date"] - pen_sales_df["Purchase Date"]).dt.days

# Calcular el tiempo medio de entrega por tipo de bolígrafo
average_delivery_time = pen_sales_df.groupby("Item")["Delivery Time"].mean().sort_values()

# Graficar el tiempo medio de entrega
plt.figure(figsize=(10, 6))
average_delivery_time.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Tiempo Medio de Entrega por Tipo de Bolígrafo", fontsize=14)
plt.xlabel("Tipo de Bolígrafo", fontsize=12)
plt.ylabel("Tiempo Medio de Entrega (días)", fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
