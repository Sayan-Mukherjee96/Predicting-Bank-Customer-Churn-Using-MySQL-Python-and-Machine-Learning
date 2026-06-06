🏦 Predicting Bank Customer Churn Using MySQL, Python, and Machine Learning 📌 Project Overview
Customer churn is a major challenge in the banking sector, directly impacting revenue and long-term profitability. Retaining existing customers is significantly more cost-effective than acquiring new ones, making early churn prediction a critical business priority.
This project focuses on predicting bank customer churn using MySQL, Python, and Machine Learning classification models. The goal is to identify customers who are likely to leave the bank, enabling targeted retention strategies.
---
🛠️ Tools & Technologies
Tool	Purpose
MySQL	Data storage, exploration, and SQL-based analysis
Python	Data preprocessing, EDA, and model development
Pandas & NumPy	Data manipulation and analysis
Matplotlib & Seaborn	Data visualization
Scikit-learn	Machine learning model building and evaluation
---
📂 Project Structure
```
Bank_Customer_Churn_Project/
├── bank_churn.ipynb                  # Full Jupyter Notebook (EDA + Modeling)
├── 01_Data_Preprocessing_&_EDA.py    # Exploratory Data Analysis & Preprocessing
├── 02_Model_Building_Evaluation.py   # Model Building & Evaluation
├── bank_churn.sql                    # MySQL Queries & Analysis
├── ML.pptx                           # Project Presentation
└── README.md                         # Project Documentation
```
---
📊 Dataset Overview
Property	Details
Total Records	10,000 customers
Total Features	13 columns
Target Variable	`Exited` (1 = Churned, 0 = Retained)
Churn Rate	20.4% churned, 79.6% retained
Key Features
Demographics — Age, Gender, Geography
Account Info — Credit Score, Balance, Number of Products
Activity — Active Member Status, Estimated Salary
Target — Exited (Churn or Not)
---
🔍 Project Workflow
1. SQL Analysis (`bank_churn.sql`)
Data exploration using MySQL queries
Basic statistical analysis and churn distribution
2. EDA & Preprocessing (`01_EDA_Preprocessing.py`)
Exploratory Data Analysis (EDA)
Outlier detection and treatment using IQR method
Feature encoding — One Hot Encoding (Geography), Label Encoding (Gender)
Feature scaling using StandardScaler
Removing unnecessary columns (CustomerID, Surname)
Correlation analysis
3. Model Building & Evaluation (`02_Model_Building_Evaluation.py`)
Train/Test split (70/30)
Three classification models built and evaluated:
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Evaluation metrics — Accuracy, Precision, Recall, F1-Score, ROC Curve, Confusion Matrix
---
🤖 Model Results
Model	Accuracy	Precision (Churn)	Recall (Churn)	F1-Score (Churn)
Logistic Regression	81%	56%	19%	29%
Decision Tree	85%	69%	42%	52%
Random Forest	87%	78%	47%	59%
🏆 Best Model — Random Forest Classifier
Highest accuracy of 87%
Best churn detection with 78% precision and 59% F1-Score
Strongest ROC curve performance among all models

📈 Key Insights
Machine learning proved to be an effective approach for customer churn prediction.
Logistic Regression served as a strong baseline model.
Decision Tree significantly improved churn detection performance.
Random Forest achieved the best overall classification performance.
Customer churn appears to be influenced by multiple factors rather than a single feature.
The final model can support proactive customer retention strategies.

💡 Recommendations
Deploy the Random Forest Classifier to identify high-risk churn customers
Implement targeted retention strategies such as personalized offers and loyalty programs
Continuously retrain the model with updated data to maintain prediction accuracy
Incorporate additional behavioral and transaction features in future model versions
---
🚀 How to Run
Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```
Run Jupyter Notebook
```bash
jupyter notebook bank_churn.ipynb
```
Run Python Scripts
```bash
python 01_Data_Preprocessing_&_EDA.py
python 02_Model_Building_Evaluation.py
```
---
👤 Author
Your Name: Sayan Mukherjee
GitHub: https://github.com/Sayan-Mukherjee96/Predicting-Bank-Customer-Churn-Using-MySQL-Python-and-Machine-Learning
LinkedIn:https://www.linkedin.com/in/sayan-mukherjee-923b6330a
Email: sayanmukherjee010196@gmail.com
