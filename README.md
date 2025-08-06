# Harshitpal1-Data-Cleaning-and-Processing-Data-Analytics
# Elevate Data Analyst Internship: Task 1 Submission

### Project: Data Cleaning and Preprocessing

**Date:** August 6, 2025

## 1. Project Overview

This repository contains the complete submission for **Task 1: Data Cleaning and Preprocessing** for the Elevate Data Analyst Internship. [cite_start]The objective was to take a raw dataset, perform necessary cleaning and preparation, and produce a final, analysis-ready dataset. [cite: 5] [cite_start]This process is a critical first step in the data analytics workflow, ensuring the quality and reliability of any subsequent analysis or modeling. [cite: 22, 24]

---

## 2. Dataset and Tools

* [cite_start]**Dataset:** [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) from Kaggle. [cite: 14] This dataset contains customer demographics, purchasing habits, and campaign responses.
* **Tools Used:**
    * [cite_start]**Language:** Python [cite: 5]
    * [cite_start]**Libraries:** Pandas for data manipulation and analysis. [cite: 5, 21]

---

## 3. Summary of Data Cleaning Steps

The data cleaning was performed using a Python script, which is included in this repository. The key steps are summarized below:

1.  **Loaded the Dataset:** The `marketing_campaign.csv` file was loaded into a Pandas DataFrame.

2.  [cite_start]**Renamed Columns:** All column headers were standardized to a consistent format (lowercase with underscores, e.g., `Year_Birth` became `year_birth`) for easier access and readability. [cite: 11]

3.  **Handled Missing Values:** The `Income` column contained 24 missing values. [cite_start]These were identified using `isnull()` [cite: 8] and filled using the **median** income of the dataset. The median was chosen over the mean to avoid being skewed by a few extremely high-income values.

4.  [cite_start]**Converted Data Types:** The `Dt_Customer` (date of customer enrollment) column was converted from a string object to a proper `datetime` format to enable date-based calculations. [cite: 10, 12]

5.  **Performed Feature Engineering:**
    * Created a new `age` column by subtracting the `year_birth` from the current year.
    * Created a `total_children` column by summing the `kid_home` and `teen_home` columns.

6.  **Standardized Categorical Data:** The `Marital_Status` column had several inconsistent or rare values (`'YOLO'`, `'Alone'`, `'Absurd'`). These were grouped into broader, more meaningful categories: `'Partner'` and `'Single'`.

7.  [cite_start]**Removed Duplicates:** The dataset was checked for any fully duplicated rows using `drop_duplicates()` [cite: 9] and none were found.

8.  **Treated Outliers:** Basic outlier filtering was applied to remove records that were likely data entry errors. This included customers with an `age` over 90 or an `income` over 250,000.

[cite_start]The final, cleaned dataset is saved as `cleaned_customer_data.csv` and is ready for analysis. [cite: 6]

---

## 4. Interview Questions & Answers

**1. [cite_start]What are missing values and how do you handle them?** [cite: 26]
Missing values are data points that are not recorded in a dataset, often represented as `NaN` or `NULL`. I handle them by first identifying them using `df.isnull().sum()`. The strategy depends on the situation:
* **Removal:** If the number of missing values is very small, I might remove the rows using `dropna()`.
* **Imputation:** If the feature is important, I fill the missing values. For numerical data, I use the **mean** or **median** (as I did with 'Income'). For categorical data, I use the **mode**.

**2. [cite_start]How do you treat duplicate records?** [cite: 27]
Duplicate records are identical rows in a dataset that can bias analysis. [cite_start]I identify them using `df.duplicated().sum()` and remove them using `df.drop_duplicates()` in Pandas to ensure every record is unique. [cite: 9]

**3. [cite_start]Difference between `dropna()` and `fillna()` in Pandas?** [cite: 28]
* `dropna()` **removes** rows or columns that contain one or more missing values.
* `fillna()` **replaces** missing values with a specified value (like the mean, median, or a constant string). It fills the gaps instead of deleting them.

**4. [cite_start]What is outlier treatment and why is it important?** [cite: 29]
Outlier treatment is the process of identifying and managing data points that are significantly different from the rest of the data. It's crucial because outliers can skew statistical results (like the mean) and negatively affect the performance of machine learning models. Treatment can involve removing the outlier or transforming the data.

**5. [cite_start]Explain the process of standardizing data.** [cite: 30]
Data standardization is the process of bringing data into a uniform format. This includes:
* Making sure text values are consistent (e.g., "USA" and "United States" become one standard).
* [cite_start]Ensuring date formats are the same (e.g., all dates are `YYYY-MM-DD`). [cite: 10]
* In machine learning, it also refers to scaling numerical features to a common range so that no single feature dominates the analysis.

**6. [cite_start]How do you handle inconsistent data formats (e.g., date/time)?** [cite: 31]
I handle inconsistent formats by converting them to a single, standard format. For dates and times, I use the `pd.to_datetime()` function in Pandas. [cite_start]This function can intelligently parse various string formats (like "04-09-2012" or "2012/09/04") and convert them into a consistent `datetime` object. [cite: 10]

**7. [cite_start]What are common data cleaning challenges?** [cite: 32]
Common challenges include:
* **Structural Errors:** Typos, inconsistent capitalization, and mixed data types in a column.
* **Missing Data:** Deciding on the best imputation strategy (mean, median, etc.).
* **Outliers:** Determining if an extreme value is a genuine data point or an error.
* **Large Datasets:** Performing cleaning operations efficiently without consuming too much memory.

**8. [cite_start]How can you check data quality?** [cite: 33]
I check data quality through **data profiling**. This involves using several Pandas functions:
* `.info()` to check data types and non-null counts.
* `.describe()` to get a statistical summary of numerical columns (mean, std, min, max).
* `.value_counts()` to inspect the unique values and their frequencies in categorical columns.
* `.isnull().sum()` to count missing values in each column.
* Creating visualizations like histograms and box plots to see the data's distribution and identify outliers.
e used for all cleaning steps[cite: 5, 21].
* **`README.md`:** This summary file.

By completing this task, I have gained practical experience in fixing common data issues and have prepared a structured dataset ready for analysis[cite: 20, 24].
