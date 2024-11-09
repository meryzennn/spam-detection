import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("data_spam.csv", encoding="latin-1")
data.head()

data = data[["class","message"]]

x = np.array(data["message"])
y = np.array(data["class"])
cv = CountVectorizer()

X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=33)

deteksi = MultinomialNB()
deteksi.fit(X_train, y_train)

inputan = input("Masukkan teks: ")
data = cv.transform([inputan]).toarray()
print(deteksi.predict(data))