# T-1Skilltixs-internship-SyedAbbas
🧹 Customer Personality Data Cleaning
This script handles initial cleaning steps on the customer_personality.csv dataset, preparing it for analysis or modeling:

1. Load Dataset
Reads the raw CSV file into a Pandas DataFrame.

2. Handle Missing Values
Displays the count of nulls in each column.

Drops any rows where Income is missing, ensuring key financial data is retained — a common strategy when missingness is minimal {CITATION_START}cite{CITATION_DELIMITER}turn0search4{CITATION_STOP}.

3. Remove Duplicates
Eliminates duplicate rows with df.drop_duplicates(), ensuring each customer record is unique for accurate analysis.

4. Standardize Text Fields
Cleans string columns like Education and Marital_Status by stripping whitespace and lowercasing text, ensuring consistent category values {CITATION_START}cite{CITATION_DELIMITER}turn0search10{CITATION_STOP}.

5. Parse Date Field
Converts Dt_Customer into a datetime format (day-first), enabling time-based feature extraction such as customer tenure {CITATION_START}cite{CITATION_DELIMITER}turn0search4{CITATION_STOP}.

6. Rename Columns
Transforms column names to lowercase with underscores, improving code readability and following a consistent naming convention.

7. Correct Data Types
Converts year_birth to integer and income to float, ensuring numeric operations behave correctly.

Adds a new age column based on the birth year to support demographic analysis.

8. Preview & Save
Displays the first few rows of the cleaned DataFrame for verification.

Optionally saves the result to cleaned_dataset.csv for use in subsequent processes.

