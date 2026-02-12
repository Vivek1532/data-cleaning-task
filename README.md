# Data Cleaning & Preprocessing Project

## 📌 Objective
The objective of this project is to clean and preprocess a raw dataset that contains missing values, duplicate records, and inconsistent formatting.  
The final output is a structured dataset ready for analysis or machine learning.

---

## 📊 Dataset
Dataset used: Mall Customer Segmentation Data (simulated raw dataset)

The dataset contains customer information such as:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

The raw dataset intentionally includes:

- Missing values
- Duplicate rows
- Inconsistent text formatting
- Extra spaces
- Mixed capitalization

These issues simulate real-world messy data.

---

## 🛠 Tools Used

- Python
- Pandas
- NumPy
- Visual Studio Code
- Git & GitHub

---

## 🔧 Data Cleaning Steps Performed

1. Identified missing values using:

   df.isnull()

2. Filled missing values:
   - Age → replaced with mean value
   - Gender → replaced with "unknown"

3. Removed duplicate records:

   df.drop_duplicates()

4. Standardized text values:
   - converted to lowercase
   - removed extra spaces

5. Renamed column headers:
   - lowercase
   - no spaces
   - consistent naming

6. Fixed data types:
   - Age converted to integer

7. Exported cleaned dataset:

   cleaned_dataset.csv

---

## ✅ Final Output

- Raw dataset → `mall_customer_segmentation_raw.csv`
- Cleaned dataset → `cleaned_dataset.csv`
- Cleaning script → `cleaning.py`

The final dataset is clean, consistent, and ready for analysis.

---

## 🎯 Skills Demonstrated

- Data preprocessing
- Handling missing values
- Removing duplicates
- Text normalization
- Data type correction
- Python scripting
- GitHub project workflow

---

## 💡 Why Data Cleaning is Important

Data cleaning improves accuracy, reliability, and model performance.  
Poor quality data leads to incorrect insights and unreliable predictions.

---

## 📂 Project Structure

data-cleaning-task/

├── cleaning.py  
├── mall_customer_segmentation_raw.csv  
├── cleaned_dataset.csv  
├── INTERVIEW_QA.md  
└── README.md  

---

## 🚀 Author

Vivek Kumar
Beginner Data Analyst / Python Learner
