# 🏥 DiagnoAI: Diagnose Smarter, Live Healthier

An AI-powered medical diagnosis system that detects multiple diseases using deep learning and machine learning models.

![Screenshot 2025-03-01 031751](https://github.com/user-attachments/assets/56ee4656-19d6-4731-afd4-8d7eaad66c70)


---

## 🔬 Disease Detections

DiagnoAI supports **7 disease detections** using advanced AI models:

| Disease            | Model Used              | Accuracy |
|-------------------|------------------------|----------|
| **Covid-19**      | CNN                     | 93%      |
| **Brain Tumor**   | CNN + VGG16             | 100%*    |
| **Breast Cancer** | Random Forest           | 91.81%   |
| **Alzheimer**     | CNN                     | 73.54%   |
| **Diabetes**      | Random Forest           | 66.8%    |
| **Pneumonia**     | CNN                     | 83.17%   |
| **Heart Disease** | XGBoost                 | 86.96%   |

> *100% accuracy was achieved on a small test set of 10 images.

Each disease module includes:
✅ **User-friendly interface** for inputting scans or medical data.  
✅ **Real-time AI predictions** using pre-trained models.  
✅ **Interpretation of results** with probability scores.  

---

## 🔑 Secure JWT Authentication

DiagnoAI implements **JSON Web Token (JWT) Authentication** to ensure:  
🔐 **Secure user access** to the system.  
📂 **Protection of medical data** from unauthorized access.  
🔄 **Session-based authentication**, requiring login for predictions.  

When a user signs up, they receive a **JWT token**, which is required for making API requests to the model. This ensures **data privacy and security**.

---

## 📸 Screenshots

#### 🔹 Login/Signup Page  

![Screenshot 2025-03-01 030108](https://github.com/user-attachments/assets/0bdb7d5d-39e5-4c66-86c7-2125e9c6861a)
![Screenshot 2025-03-01 030145](https://github.com/user-attachments/assets/f745d80a-a779-4077-a32d-913c26cb18d1)
![Screenshot 2025-03-01 030253](https://github.com/user-attachments/assets/8434484c-61ec-46db-9ea2-8bc442790e05)

#### 🔹 Disease Detection  

Covid-19 Detection
![Screenshot 2025-03-01 031837](https://github.com/user-attachments/assets/2ce120ee-a1ab-4fe9-9801-d785aa189026)

Brain Tumor Detection
![Screenshot 2025-03-01 031951](https://github.com/user-attachments/assets/595bc1d9-4771-41eb-9146-2baadf986f74)

Breast Cancer Detection
![Screenshot 2025-03-01 032151](https://github.com/user-attachments/assets/6f983d36-3bd9-4a24-afe3-51dcee29c580)

Alzheimer Detection
![Screenshot 2025-03-01 032300](https://github.com/user-attachments/assets/bceb00ea-f639-457e-bea6-f142880776c5)

Pneumonia Detection

![Screenshot 2025-03-01 032519](https://github.com/user-attachments/assets/eb942a76-1cbc-4df8-ac12-14a56471cedf)

Heart Disease Detection
![Screenshot 2025-03-01 032618](https://github.com/user-attachments/assets/e3d2362a-7876-4dbf-8694-35b795b264ff)

#### 🔹 Prediction Results  
Covid-19 Detection
![Screenshot 2025-03-01 031854](https://github.com/user-attachments/assets/2728e116-7ebf-4bcc-b177-0f40ca437100)
Brain Tumor Detection
![Screenshot 2025-03-01 032006](https://github.com/user-attachments/assets/d6e6e306-3860-473a-a898-94b773d804aa)
Breast Cancer Detection
![Screenshot 2025-03-01 032206](https://github.com/user-attachments/assets/b85bb2f7-764a-4fca-9f10-a63161ae99a3)
Alzheimer Detection
![Screenshot 2025-03-01 032314](https://github.com/user-attachments/assets/7240cb79-aeff-4e21-9596-55a47e7370c9)

Diabetes Detection
![Screenshot 2025-03-01 032438](https://github.com/user-attachments/assets/9d0f3a18-b805-4428-9fa2-06fd7edb7916)

Pneumonia Detection
![Screenshot 2025-03-01 032531](https://github.com/user-attachments/assets/276d4c95-819a-41ca-8cef-f58dc2a9f7dd)

Heart Disease Detection
![Screenshot 2025-03-01 032636](https://github.com/user-attachments/assets/1abd31d1-0c94-4392-8044-0f7ba8d3dfa8)
---


## 🚀 How to Run

### 1️⃣ **Create a Conda Environment & Install Dependencies**
```sh
conda create -n diagnoai python=3.9.13  
conda activate diagnoai  
pip install opencv-python==4.5.1.48 numpy tensorflow==2.12.0 scikit-learn==0.24.2 imutils==0.5.4 flask==3.0.0 xgboost==2.0.3
```
  
### 2️⃣ **Run the Flask Server**
```sh
flask run
```

The system will be available at:  
🔗 `http://127.0.0.1:5000/`

---

## 🔮 Future Improvements

📌 **Increase Model Accuracy** with larger datasets.  
📌 **Expand Detection Capabilities** for more diseases.  
📌 **Add Preventive Measures** based on diagnosis.  
📌 **Store Patient History** for future reference.  

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

💡 **Developed with AI-ML & Passion 💙**
