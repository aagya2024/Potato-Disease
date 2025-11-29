import React, { useState } from "react";
import axios from "axios";

export function ImageUpload() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handlePredict = async () => {
    if (!selectedImage) {
      alert("Please upload an image first.");
      return;
    }

    setLoading(true);
    setPrediction("");

    const formData = new FormData();
    formData.append("file", selectedImage);

    try {
      const res = await axios.post(
        "http://localhost:8000/predict",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setPrediction(
        `Prediction: ${res.data.class} (Confidence: ${(res.data.confidence * 100).toFixed(2)}%)`
      );
    } catch (error) {
      console.log("❌ FRONTEND ERROR:", error);
      alert("Error sending file to server");
    }

    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>Potato Disease Classifier</h2>

      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
      />

      {preview && (
        <div>
          <img
            src={preview}
            alt="preview"
            width="300"
            style={{ marginTop: "20px", borderRadius: "10px" }}
          />
        </div>
      )}

      <button
        onClick={handlePredict}
        style={{
          marginTop: "20px",
          padding: "10px 20px",
          background: "green",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
      >
        Upload & Predict
      </button>

      {loading && <p>Predicting...</p>}

      {prediction && (
        <p style={{ marginTop: "20px", fontWeight: "bold" }}>
          {prediction}
        </p>
      )}
    </div>
  );
}
