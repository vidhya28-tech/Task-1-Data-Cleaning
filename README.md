# Data Cleaning and Preprocessing

## Dataset

Customer Personality Analysis (`marketing_campaign.csv`)

The dataset was obtained from Kaggle and used to practice data cleaning and preprocessing using Python and Pandas.

## Objective

The main objective of this project is to clean and prepare the customer dataset by handling missing values, duplicate records, inconsistent categories, date formatting, and data types.

## Tools Used

* Python
* Pandas
* CSV

## Data Cleaning Steps

### 1. Handling Missing Values

* Checked the dataset for missing values.
* Found 24 missing values in the `income` column.
* Filled the missing income values using the median income of `51381.50`.

### 2. Checking Duplicate Records

* Checked the dataset for duplicate rows.
* No duplicate records were found.
* Total duplicate rows: 0.

### 3. Standardizing Column Names

* Converted column names to lowercase.
* Used underscores to make the column names consistent and easier to work with.

### 4. Cleaning Text Values

* Removed unnecessary spaces from text values.
* Standardized unusual values in the `marital_status` column:

  * `Alone` → `Single`
  * `Absurd` → `Other`
  * `YOLO` → `Other`

### 5. Date Formatting

* Converted `dt_customer` into a datetime format for validation.
* Standardized the date format to `dd-mm-yyyy`.

### 6. Data Types

* Checked the data types of the columns.
* Converted appropriate columns to numeric data types using Pandas.

## Dataset Details

| Description             | Value |
| ----------------------- | ----: |
| Rows before cleaning    |  2240 |
| Rows after cleaning     |  2240 |
| Columns before cleaning |    29 |
| Columns after cleaning  |    29 |
| Missing income values   |    24 |
| Duplicate rows          |     0 |
| Invalid dates           |     0 |

## Project Files

```text
Task-1-Data-Cleaning/
|
|-- data/
|   |-- marketing_campaign_raw.csv
|   |-- marketing_campaign_cleaned.csv
|
|-- data_cleaning.py
|-- README.md
```

## How to Run

Install Pandas:

```bash
pip install pandas
```

Run the Python script:

```bash
python data_cleaning.py
```

## Result

The dataset was cleaned and standardized using Python and Pandas. Missing values were handled, duplicate records were checked, text categories were standardized, dates were formatted, and appropriate data types were applied.
