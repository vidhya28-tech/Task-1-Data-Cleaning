# Data Cleaning and Preprocessing

## Dataset

**Customer Personality Analysis** (`marketing_campaign.csv`)

The dataset was obtained from Kaggle and used for practicing data cleaning and preprocessing with Python and Pandas.

## Objective

Clean and preprocess a raw customer dataset containing missing values, duplicate records, inconsistent text categories, date formatting issues, and data-type requirements.

## Tools Used

- Python
- Pandas
- CSV

## Cleaning Performed

1. **Missing Values**
   - Checked missing values using Pandas.
   - The `income` column contained 24 missing values.
   - Missing income values were filled using the median income of 51381.50.

2. **Duplicate Records**
   - Checked for exact duplicate rows.
   - Duplicate rows found: 0.
   - Therefore, no duplicate rows needed to be removed.

3. **Column Names**
   - Renamed column headers to lowercase.
   - Standardized column names using underscores for consistency.

4. **Text Standardization**
   - Removed leading and trailing whitespace from text values.
   - Standardized unusual `marital_status` categories:
     - `Alone` → `Single`
     - `Absurd` → `Other`
     - `YOLO` → `Other`

5. **Date Formatting**
   - Converted `dt_customer` to a datetime format for validation.
   - Standardized the saved date values to `dd-mm-yyyy` format.

6. **Data Types**
   - Converted appropriate numeric fields to numeric data types using Pandas.

## Before and After

| Description | Result |
|---|---:|
| Raw dataset rows | 2240 |
| Cleaned dataset rows | 2240 |
| Raw columns | 29 |
| Cleaned columns | 29 |
| Missing income values handled | 24 |
| Duplicate rows removed | 0 |
| Invalid dates after parsing | 0 |

## Files

- `data/marketing_campaign_raw.csv` - Original dataset copy
- `data/marketing_campaign_cleaned.csv` - Cleaned dataset
- `data_cleaning.py` - Python script used for cleaning and preprocessing

## How to Run

Install Pandas using:

```bash
pip install pandas
