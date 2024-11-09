from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load data and model components
data = pd.read_csv("data_spam.csv", encoding="latin-1")
data = data[["class", "message"]]
x = np.array(data["message"])
y = np.array(data["class"])

cv = CountVectorizer()
X = cv.fit_transform(x)

deteksi = MultinomialNB()
deteksi.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_message = data["message"]
    transformed_input = cv.transform([input_message]).toarray()
    prediction = deteksi.predict(transformed_input)
    
    result = "spam" if prediction == "spam" else "ham"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)