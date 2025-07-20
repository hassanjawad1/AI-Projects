# 📱 Screen Time & Children: A Machine Learning Deep Dive

**Can we predict the health impacts of screen time on children using data science?**  
Yes. And here’s the project that does just that.

---

## 🚀 Overview

This repository is the complete codebase and analysis for a machine learning project that explores screen time behavior in children aged 10–18, using a real-world dataset of **9,712** entries.

We applied both classic ML (Random Forest, XGBoost) and deep learning (Autoencoders for anomaly detection) to uncover hidden patterns and predict health impacts like:

- 😴 Poor Sleep  
- 👁️ Eye Strain  
- 😰 Anxiety  

The goal? To use data science for good—giving parents, educators, and health professionals deeper insight into modern screen habits.

---

## 📦 Dataset

The dataset includes:

- `Age`
- `Gender`
- `Avg_Daily_Screen_Time_hr`
- `Primary_Device` (TV / Laptop / Smartphone)
- `Exceeded_Recommended_Limit` (True/False)
- `Educational_to_Recreational_Ratio`
- `Health_Impacts` (multi-label: Poor Sleep, Anxiety, Eye Strain)
- `Urban_or_Rural`

🔍 We engineered new features, handled missing data, and converted multi-label health outcomes into separate binary columns.

---

## 🧪 Models Used

### 🎯 Target Variable: `Poor Sleep`

We trained models to predict whether a child is at risk for poor sleep based on their screen usage patterns.

### ✅ Models Trained:

- **Random Forest Classifier**  
  Easy to interpret, great baseline model.

- **XGBoost Classifier**  
  High-performing, robust to noise, and great at picking up subtle interactions.

- **Autoencoder (Deep Learning)**  
  Used for anomaly detection—flagging unusual behavioral patterns that deviate from the norm.

---

## 📊 Key Visualizations

- Correlation heatmaps  
- Bar plots comparing screen time across devices, gender, and location  
- ROC curves comparing model performance  
- Anomaly score rankings for behavioral outliers  

<p align="center">
  <img src="your-preview-image-path.png" width="600" alt="Screen Time Analysis Preview">
</p>

---

## 📈 Performance Metrics

| Model            | Accuracy | ROC AUC | Precision | Recall |
|------------------|----------|---------|-----------|--------|
| Random Forest    | ~82%     | 0.86    | 0.79      | 0.81   |
| XGBoost          | ~87%     | 0.91    | 0.85      | 0.88   |

XGBoost outperformed Random Forest across the board.

---

## 🧠 Insights

- 📱 Smartphone usage correlates most with negative health impacts  
- 🧒 Urban kids report more health issues than rural ones  
- ⏰ Kids with >6 hrs screen time are 2x more likely to suffer sleep issues  
- 🎓 Higher educational-to-recreational ratio = lower health risk  

---
## 📚 Blog
A full write-up is available on Medium

## 🧠 Future Work
- Build a parent-facing web app for real-time predictions

- Add time-series tracking for longitudinal behavior

- Collect new data on social media usage and emotional wellness


# 🙋‍♂️ Author
- Jawad Jamali
- Data Whisperer, AI Tinkerer, and believer in tech-for-good.
