# Task 1 - Data Cleaning and Preprocessing

## Dataset
**Customer Personality Analysis** (`marketing_campaign.csv`)

The dataset was obtained from Kaggle and used for practicing data cleaning and preprocessing with Python and Pandas.

## Objective
Clean a raw customer dataset containing missing values, duplicate records, inconsistent text categories, date formatting issues, and data-type requirements.

## Tools
- Python
- Pandas
- CSV

## Cleaning Performed

1. **Missing values**
   - Checked missing values using Pandas.
   - The `income` column contained 24 missing values.
   - Missing income values were filled with the median income: 51381.50.

2. **Duplicate records**
   - Checked for exact duplicate rows.
   - Duplicate rows found: 0.
   - The dataset therefore required no duplicate-row removal.

3. **Column names**
   - Renamed headers to lowercase, uniform names using underscores.

4. **Text standardization**
   - Removed leading/trailing whitespace.
   - Standardized unusual `marital_status` labels:
     - `Alone` -> `Single`
     - `Absurd` -> `Other`
     - `YOLO` -> `Other`

5. **Date formatting**
   - Converted `dt_customer` to a datetime value for validation.
   - Saved it consistently in `dd-mm-yyyy` format.

6. **Data types**
   - Converted numeric fields to numeric types using Pandas.

## Before and After
- Raw dataset rows: 2240
- Cleaned dataset rows: 2240
- Raw columns: 29
- Cleaned columns: 29
- Missing income values handled: 24
- Duplicate rows removed: 0
- Invalid dates after parsing: 0

## Files
- `data/marketing_campaign_raw.csv` - raw dataset copy
- `data/marketing_campaign_cleaned.csv` - cleaned dataset
- `data_cleaning.py` - reproducible cleaning script

## How to Run

```bash
pip install pandas
python data_cleaning.py
```

## Note
The cleaning decisions are documented so the process can be reproduced and reviewed.
