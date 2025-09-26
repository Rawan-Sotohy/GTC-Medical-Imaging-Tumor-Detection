# 🧠 GTC Medical Imaging Tumor Detection

<p align="center">
  <img src="https://previews.123rf.com/images/prockopenko/prockopenko1806/prockopenko180600051/104606657-brain-tumor-cancer-banner-symptoms-vector-signs.jpg" width="800" height="400"/>
</p>



## 📌Description

Brain tumor diagnosis from MRI images is time-consuming and prone to human error.
This project develops a deep learning model that automatically classifies MRI scans into **tumor** or **no tumor**, helping doctors speed up detection and reduce misdiagnosis.

---

## 🗂️ Dataset

The dataset comes from [Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) and contains MRI scans classified into **four categories**:

* Glioma
* Meningioma
* Pituitary
* No Tumor

**Structure:**

```
train/       -> Training images
test/        -> Testing images
```

---
## 📈 Project Workflow:

Phase 1: Data Preparation

Phase 2: Exploratory Data Analysis (EDA) & Feature Engineering

Phase 3: Model Training & Validation

Phase 4: Deployment via Web Interface

---
## 🧠 Models Implemented

We trained three models:

1. **SVM on Extracted Features**
2. **CNN from Scratch**
3. **MobileNetV2 (Transfer Learning)**

Chosen Model for Deployment: **CNN from Scratch**

---
## 🌐 Live Demo

You can try the web application here:

Brain Tumor Detection App 👉 [Live Demo](https://braintumordetection2025.streamlit.app)

---

## ⚙️ How to Run

There are **2 ways** to run this project:

### 1️⃣ Clone the Repository

If you want to download the project and run it locally:

**Open a terminal then Clone the repo**

```bash
git clone https://github.com/Rawan-Sotohy/GTC-Medical-Imaging-Tumor-Detection.git
cd GTC-Medical-Imaging-Tumor-Detection
```
**Install dependencies**

```bash
pip install -r requirements.txt
```
**Run the Streamlit app locally**

```bash
streamlit run app.py
```

### 2️⃣ Run on Google Colab

This is the easiest way to run the project without local setup:

1. **Get the Notebook**

   * Open [Google Colab](https://colab.research.google.com/)
   * Upload the project notebook (`.ipynb`)

2. **Kaggle API Token**

   * Go to [Kaggle Account Settings](https://www.kaggle.com/settings/account)
   * Create new API token → downloads `kaggle.json`

3. **Upload `kaggle.json`**

   * In Colab, run the first cell to upload the file → allows automatic dataset download

---

## 👩‍💻 Team Members

* [Aya Ayman](https://github.com/ayahayman)
* [Hoor Ashraf](https://github.com/hoorashraf55)
* [Maysoun Hassan](https://github.com/maysoun465)
* [Rawan Sotohy](https://github.com/Rawan-Sotohy)
* [Sama Mobtasem](https://github.com/sama690)
* [Sama Samer](https://github.com/sama-samer)

---
## 🎬 Media & Presentation

- **Demo Video** [Watch the Video](https://drive.google.com/file/d/10gHk87adc20HMj3J8ibwIQ5P1Wr7nGOx/view?usp=drive_link)
- **Presentation:** [View the Presentation](https://www.canva.com/design/DAGz-t3wV2k/Ugsqc22FZj6EBGOxhOa9Cg/edit?utm_content=DAGz-t3wV2k&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
---

**This project was developed under the supervision of GTC.**
