import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt  # gráficos
import string  # para limpiar texto

# cargar datos
file_path = "./Data/Pen Sales Data.xlsx"
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

# --- Tarea 5: Sentimiento de reseñas ---
pen_sales_df["Review"] = pen_sales_df["Review"].fillna("")
positive_words = ["love", "great", "good", "amazing", "excellent", "best"]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

def preprocess_text(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text.split()

pos, neg = 0, 0
for review in pen_sales_df["Review"]:
    words = preprocess_text(review)
    pos += sum(w in positive_words for w in words)
    neg += sum(w in negative_words for w in words)

plt.figure(figsize=(8, 8))
plt.pie([pos, neg], labels=["Positive", "Negative"], colors=["#4CAF50","#F44336"],
        explode=(0.1,0), autopct="%1.1f%%", startangle=140)
plt.title("Sentiment Analysis")
plt.show()
