import joblib
import requests
from sklearn.feature_extraction.text import CountVectorizer
from fastapi import FastAPI
from pydantic import BaseModel

# Unduh model dari cloud storage (jika belum ada di server)
def load_model():
    try:
        deteksi = joblib.load('spam_detector.pkl')
    except:
        model_url = "https://drive.google.com/file/d/1ifP7pBUWzU6yfR51d417lx3O5yaXoMij/view?usp=sharing"
        model_file = requests.get(model_url)
        with open('spam_detector.pkl', 'wb') as f:
            f.write(model_file.content)
        deteksi = joblib.load('spam_detector.pkl')
    return deteksi

# FastAPI untuk membuat API
app = FastAPI()

class InputText(BaseModel):
    message: str

@app.post("/deteksi-spam")
def predict(input_data: InputText):
    # Load model
    deteksi = load_model()

    # Transform input message into feature vector
    cv = CountVectorizer()
    data = cv.transform([input_data.message]).toarray()

    # Prediksi
    prediction = deteksi.predict(data)
    return {"prediction": prediction[0]}
