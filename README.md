### Sales Data Analysis and Feature Engineering
This project focuses on analyzing sales data from CSV files (brands, products, stores, and sales) and performing feature engineering to enhance the dataset for further analysis or modeling tasks.

### Overview
The script loads data from CSV files containing information about brands, products, stores, and sales transactions. It integrates these datasets, converts necessary columns, and filters the data based on a specified date range provided via command-line arguments.

### Feature Engineering
The script performs the following feature engineering tasks:

- Calculates rolling averages (7-day window) and lagged values for product sales (MA7_P, LAG7_P), brand sales (MA7_B, LAG7_B), and store sales (MA7_S, LAG7_S).
- Aggregates sales data by product, brand, and store to derive insights into trends and historical performance.

### Dependencies
- pandas
- numpy
- argparse
