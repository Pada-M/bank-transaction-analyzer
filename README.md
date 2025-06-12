# Bank Customer Transaction Analyzer

This project analyzes mock bank customer transaction data using Python, SQLite, SQL, and data visualization tools. It demonstrates how to load transaction data, perform SQL queries for insights, and visualize spending patterns by category and customer.

---

## Features

- Load transaction data from CSV
- Store data in SQLite database
- Run SQL queries to summarize spending by category and by customer
- Visualize results with bar charts using Seaborn and Matplotlib

---

## Technologies Used

- Python 3
- Pandas
- SQLite3
- Seaborn
- Matplotlib

---

## Setup and Usage

1. Clone this repository (or download project files)


2. Install required Python packages

  pip install pandas seaborn matplotlib

3. Prepare your data
  python .\generate_data.py


4. Run the analyzer script

  python .\analyzer.py

The script will:

- Load the CSV data
- Insert data into SQLite database (data/transactions.db)
- Run SQL queries to summarize spending
- Display bar charts showing spending by category and by customer

---

## Contact

If you have questions or feedback, feel free to reach out at: pjmayer@ualberta.ca

