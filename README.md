![image](https://github.com/user-attachments/assets/b1d56b4f-00fd-4992-8ca8-83317825700a)

# 🏥 Cirrhosis Outcome Prediction: Forecasting Patient Outcomes  


### **TL;DR**  
Applied **multi-class classification** to predict patient outcomes in cirrhosis. Leveraged **feature engineering, outlier removal, and an ensemble modeling approach** to improve accuracy. Currently **ranked with a log loss of 0.37136**. 🚀  

---

## 📌 Project Overview  
This competition involves **multi-class classification** to predict patient outcomes in cirrhosis. The goal is to develop a **highly accurate model** that predicts three possible outcomes:  
- **Status_C** – Patients censored 
- **Status_CL** – Patients censored due to liver transplantation 
- **Status_D** – Patients deceased

Our approach includes **advanced feature engineering, outlier handling, and model stacking** to optimize predictions.

---

## **🎯 Approach & Methodology**

### **🔹 Feature Engineering Strategy**  
Instead of simply using raw clinical features, we enhanced the dataset with **derived features** based on domain knowledge to capture better **biological relationships**.

<!--#### **🔬 Feature Transformations**-->

🚧 Pending Publication 

<!-- ✅ **Feature Ratios for Clinical Relevance**  
- Bilirubin-to-Albumin Ratio to capture liver function balance.

✅ **Binary Indicators for Critical Biomarker Levels**  
- Flags for high bilirubin and low albumin to indicate potential complications.

✅ **Log Transforming Skewed Features**  
- Normalizing highly skewed variables (Bilirubin, SGOT, Alk_Phos, Copper) for better interpretability. -->

---

## **📊 Feature Importance**

Understanding which features contribute most to the model's decision-making is **critical** for interpretability. Below is the **feature importance plot**, which highlights the most influential variables in predicting cirrhosis outcomes.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/aeb49a00-6a70-4848-857a-6beebefc33ee" width="600"></td>
  </tr>
</table>

---

## **🧪 Data Processing & Feature Engineering**  



### **📊 Data Preprocessing Steps:**  

🚧 Pending Publication 

<!--✅ **Handled Missing Values** – Imputed numerical and categorical missing values  
✅ **One-Hot Encoding** – Converted categorical variables into model-friendly features  
✅ **Log Transformation** – Applied log-scaling to skewed variables for better feature distribution  -->


## **📈 Model Performance**  

🚧 Pending Publication 

<!--Feature engineering consistently improved model accuracy.  
A **stacking model** (XGBoost, LightGBM, and CatBoost) was trained to minimize **multi-class log loss**.

| Model         | Log Loss Before | Log Loss After  |
|--------------|---------------|---------------|
| **XGBoost**   | 0.7269        | 0.3713        |
| **LightGBM**  | 0.6892        | 0.3589        |
| **CatBoost**  | 0.7021        | **0.3404**    |
| **Stacked**   | 0.6931        | **0.3287**    |

🔹 **Final approach used a stacked model** combining XGBoost, LightGBM, and CatBoost for optimal predictions.  
🔹 **Ensemble methods helped improve generalization** and reduce variance.   -->

---

## **🔎 Findings & Next Steps**  
1️⃣ **Feature engineering significantly improved model performance.**  
2️⃣ **Log transformation reduced skewness in key clinical features.**  
3️⃣ **Future Work:** Experimenting with **hyperparameter tuning**, additional feature interactions, and ensemble techniques.

### **🏆 Kaggle Score: 0.37136** (Rank #1 in the competition so far 🎉)  

---

## **🏁 Conclusion**  
This project demonstrates the power of **domain-driven feature engineering** and **ensemble modeling** in improving medical outcome predictions.  
  


![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=autumnmarin.cirrhosis)
