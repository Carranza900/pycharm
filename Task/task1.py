import pandas as pd
import matplotlib.pyplot as plt

# Datos de ventas
data = {
    'product':  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'category': ['Electrónica', 'Hogar', 'Electrónica', 'Deportes', 'Hogar', 'Juguetes', 'Deportes', 'Electrónica', 'Juguetes', 'Hogar'],
    'ventas': [500, 300, 700, 200, 400, 100, 350, 900, 150, 600]
}

df_ventas = pd.DataFrame(data)

# Agrupar ventas por categoría
ventas_por_categoria = df_ventas.groupby('category')['ventas'].sum()

# Gráfico de barras
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')
plt.title('Ventas Totales por Categoría (Barras)')
plt.xticks(rotation=0) #hace que el label lo deje de manera horizontal, osea el titulo para cambiarlo de posición
plt.grid(axis='y', linestyle='--', alpha=0.7) # pinta las lineas de manera descontinuas en el eje y
plt.show() # se encarga de reenderizar

# Gráfico de líneas
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind='line', marker='o', linestyle='-', color='green')
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')
plt.title('Ventas Totales por Categoría (Líneas)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


#Gráfico de pastel
plt.figure(figsize=(6, 6))
ventas_por_categoria.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'red', 'green', 'orange'])
plt.ylabel('')  # Oculta el label del eje Y
plt.title('Distribución de Ventas por Categoría (Pastel)')
plt.show()

#autopct:


#plt es un alias, es como un lienzo donde vamos a pintar el diagrama
# (8,5) representa las pulgadas de ancho y alto(osea las medidas del lienzo donde se va a representar el diagrama)
#Grupby tomamos el dataset y obtenemos los valores unicos
#necesitamos usar el sum, entonces necesitamos usar un metodo de agregado

df_ventas.to.csv