# Potato Disease

This is a CNN based potato disease classification system using TensorFlow and FastAPI.The main goal is to classify whether a potato leaf is Healthy, Early Blight, or Late Blight. The model is trained on potato leaf images using real time augmentation to improve generalization. After achieving high accuracy the model is integrated into a FastAPI backend that accepts uploaded images and returns predictions in JSON format. The complete pipeline from dataset preprocessing to API deployment makes this an end to end machine learning project ready for real world use.


**Features**

-> CNN based multiclass image classifier

->Real time data augmentation for better generalization

->Preprocessing pipeline with resizing, normalization and one-hot encoding

->FastAPI backend for real time predictions

->JSON based output with class label and confidence score


**Workflow**

->Dataset Preprocessing

->Data Augmentation

->Rescale (1/255), rotations, zoom, flips, shifting and more

->CNN Model Building and Training

->Evaluation and Saving the Model

->FastAPI Integration for Inference


**Image Preprocessing**

->Resize = 256×256

->Convert = RGB

->Normalize = [0,1]

->Encode labels = One hot


**Prediction Flow**

->User uploads an image

->API reads -> preprocesses (resize, normalize)

->Model performs inference

->API returns JSON with:

1)Predicted Class

2)Confidence Score
