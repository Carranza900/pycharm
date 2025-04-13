import pandas as pd  # manejo de datos
import matplotlib.pyplot as plt  # gráficos
import string  # para limpiar texto

# cargar datos
file_path = "../Data/Pen Sales Data.xlsx"
pen_sales_df = pd.read_excel(file_path, sheet_name="Pen Sales")


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
