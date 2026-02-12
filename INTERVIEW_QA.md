# Interview Questions – Data Cleaning Task

## 1. What are missing values and how do you handle them?

Missing values are empty or null entries in a dataset.
They can be handled by removing rows or filling them using mean, median, or mode depending on the situation.

---

## 2. How do you treat duplicate records?

Duplicate records are removed using drop_duplicates() to avoid repeated data and biased analysis.

---

## 3. Difference between dropna() and fillna()

dropna() removes rows with missing values.
fillna() replaces missing values with a chosen value.

---

## 4. What is outlier treatment and why is it important?

Outliers are extreme values that distort analysis.
Removing or treating outliers improves accuracy and model performance.

---

## 5. Explain the process of standardizing data

Standardizing data means making values consistent.
Example: converting Male, MALE, male → male.

---

## 6. How do you handle inconsistent date formats?

Using pandas datetime conversion:

pd.to_datetime()

This ensures proper date analysis.

---

## 7. What are common data cleaning challenges?

Missing values, duplicates, inconsistent formatting, wrong data types, and outliers.

---

## 8. How can you check data quality?

Using:
.info()
.describe()
.isnull().sum()
.duplicated()

These functions help identify data issues.
