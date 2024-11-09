import pandas as pd
import numpy as np
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load data and train model
data = pd.read_csv("data_spam.csv", encoding="latin-1")
data = data[["class", "message"]]

x = np.array(data["message"])
y = np.array(data["class"])
cv = CountVectorizer()

X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=33)

deteksi = MultinomialNB()
deteksi.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_spam', methods=['POST'])
def check_spam():
    message = request.form['message']
    data = cv.transform([message]).toarray()
    prediction = deteksi.predict(data)
    return jsonify({'is_spam': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)