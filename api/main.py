from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# ALWAYS WORKS → Use ABSOLUTE PATH
# ===============================

MODEL_DIR = r"C:/Users/Aagya/Desktop/potato_disease/models"

keras_files = [f for f in os.listdir(MODEL_DIR) if f.endswith(".keras")]

if not keras_files:
    print("❌ No .keras model found.")
    MODEL = None
else:
    latest_model = sorted(keras_files, key=lambda x: int(x.split(".")[0]))[-1]
    MODEL_PATH = os.path.join(MODEL_DIR, latest_model)

    print("📦 Loading model:", MODEL_PATH)
    MODEL = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully.")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]


@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).resize((256, 256))
    return np.array(image)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if MODEL is None:
        return {"error": "Model not loaded"}

    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    prediction = MODEL.predict(img_batch)[0]

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "class": predicted_class,
        "confidence": confidence
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
