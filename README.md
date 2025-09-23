# GTC Medical Imaging Tumor Detection

📌 Description

Brain tumor diagnosis from medical images is time-consuming and prone to human error.  
This project develops a deep learning model that automatically classifies MRI scans as **tumor** or **no tumor**, helping doctors speed up detection and reduce misdiagnosis.  

---

👩‍💻 Team Members
- [Aya Ayman](https://github.com/ayahayman)  
- [Hoor Ashraf](https://github.com/hoorashraf55)  
- [Maysoun Hassan](https://github.com/maysoun465)  
- [Rawan Sotohy](https://github.com/Rawan-Sotohy)  
- [Sama Mobtasem](https://github.com/sama690)  
- [Sama Samer](https://github.com/sama-samer)
---
# 🧠 Brain Tumor MRI DataSet

This dataset has 2 files train and test each classify brain MRI images into four categories:
- **Glioma**
- **Meningioma**
- **Pituitary**
- **No Tumor**

The dataset comes from Kaggle.

---

## How to Run

### 1. Get the Notebook
- Open [Google Colab](https://colab.research.google.com/).
- Upload the notebook file with (`.ipynb`).

### 2. Get Kaggle API Token
- Go to your [Kaggle Account Settings](https://www.kaggle.com/settings/account).
- Scroll down to **API** and click **Create New API Token**.
- This will download a file called `kaggle.json`.

### 3. Upload `kaggle.json` to Colab
- In the notebook, run the first cell (it will ask you to upload the file).
- This allows the notebook to download the dataset automatically.

### 4. Install Dependencies
- Make sure to install the required Python libraries:

### 5. Spliting Data
- We split the train file into a training set and validation set while the test set is the same file as it is

### 6. Resizing and Normalizing
- We make sure it is Grayscale by forcing it to be 1 Channel and we resize the file to be (128*128) then we change the PIL images to Arrays using toTensor() to do the normalization

### 7. Checking Range 
- We make sure the sets are with a range of [0,1]

### 8. Data Augmentation
We apply slight brightness adjustment, horizontal flipping, and random rotation within ±15°

---
## Model Training
We experimented with different models for brain tumor classification:

### 1️⃣ SVM on Extracted Features
- **Input:** Flattened features from images  
- **Scaling:** StandardScaler  
- **Kernel:** Linear  
- **Test Accuracy:** 0.6625  
- **Strengths:** Fast to train, simple baseline  
- **Weaknesses:** Limited performance compared to CNNs

### 2️⃣ CNN from Scratch
- **Input Size:** 128×128×3  
- **Layers:** 2 Conv layers + MaxPooling, 1 Dense (128) + Dropout 0.5  
- **Epochs:** 10  
- **Test Accuracy:** 0.9603
- **Strengths:** Simple, relatively fast, good performance  
- **Weaknesses:** Might underperform on larger datasets

### 3️⃣ MobileNetV2 (Transfer Learning)
- **Input Size:** 128×128×3  
- **Pretrained on:** ImageNet  
- **Trainable Layers:** Top classifier only  
- **Epochs:** 10  
- **Test Accuracy:** 0.8764  
- **Strengths:** Lightweight, fast training, good accuracy  
- **Weaknesses:** Slightly lower performance than CNN from scratch in this dataset

### 4️⃣ ResNet50 (Transfer Learning)
- **Input Size:** 224×224×3  
- **Pretrained on:** ImageNet  
- **Trainable Layers:** Top classifier only  
- **Epochs:** 10  
- **Test Accuracy:** 0.6346 
- **Strengths:** Very accurate on large datasets  
- **Weaknesses:** Very slow, high GPU/memory requirements  

