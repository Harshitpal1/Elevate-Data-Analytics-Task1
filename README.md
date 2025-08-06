# Harshitpal1-Data-Cleaning-and-Processing-Data-Analytics
# Elevate Data Analyst Internship: Task 1

## Data Cleaning and Preprocessing of the Customer Personality Analysis Dataset

[cite_start]This repository contains the solution for Task 1 of the Elevate Data Analyst Internship[cite: 1]. [cite_start]The objective of this task was to perform data cleaning and preprocessing on a raw dataset[cite: 5].

### 1. Dataset Used

* [cite_start]**Name:** Customer Personality Analysis [cite: 14]
* **Source:** Kaggle
* **Description:** This dataset contains information about customers, including their demographics, product purchases, and campaign responses. It is a suitable choice as it presents several common data quality issues.

### 2. Tools Used

* [cite_start]**Language:** Python [cite: 5]
* [cite_start]**Library:** Pandas [cite: 5, 21]

### 3. Data Cleaning and Preprocessing Steps

A Jupyter Notebook (`data_cleaning.ipynb`) is included in this repository with the full Python code. [cite_start]The following is a summary of the key changes made to the dataset[cite: 6]:

* **Handling Missing Values:**
    * [cite_start]I identified missing values in the 'Income' column using the `isnull().sum()` method.
    * Given that 'Income' is a numerical column, I chose to fill the missing values with the median income. This approach avoids distortion from a few very high or low-income outliers.

* **Renaming Column Headers:**
    * [cite_start]To ensure consistency and ease of use, I renamed all column headers to be more uniform[cite: 11]. For example, `Dt_Customer` was changed to `date_customer`.

* **Data Type Conversion:**
    * [cite_start]I checked the data types of all columns using `.info()`.
    * [cite_start]The `date_customer` column was converted from an 'object' type to a 'datetime' type to enable proper time-series analysis.

* **Feature Engineering (Data Standardization):**
    * I created a new feature called `age` from the `Year_Birth` column for easier analysis.
    * I standardized several categorical features by creating new, more intuitive columns. For instance, I created a `marital_status` column that simplifies the categories from the original `Marital_Status` feature.
    * I created a `total_children` feature by combining the `Kidhome` and `Teenhome` columns.

* **Removing Duplicate Rows:**
    * [cite_start]I checked for duplicate rows using `duplicated().sum()` and removed them using the `drop_duplicates()` function to ensure each record is unique.

* **Outlier Treatment:**
    * I identified potential outliers in the `age` and `Income` columns using box plots.
    * For this analysis, I decided to keep the outliers but documented their presence, as they could represent valid high-income earners or older customers. [cite_start]This is a critical step before performing analysis.

### 4. Deliverables

* **`/datasets` folder:** Contains the original raw dataset and the final cleaned dataset.
* [cite_start]**`data_cleaning.ipynb`:** The Jupyter Notebook with the Python (Pandas) code used for all cleaning steps[cite: 5, 21].
* **`README.md`:** This summary file.

By completing this task, I have gained practical experience in fixing common data issues and have prepared a structured dataset ready for analysis[cite: 20, 24].
