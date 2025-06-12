import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Step 1: Load CSV file
    df = pd.read_csv("data/mock_transactions.csv")
    print("Loaded CSV:")
    print(df.head())

    # Step 2: Load data into SQLite
    conn = sqlite3.connect("data/transactions.db")
    df.to_sql("transactions", conn, index=False, if_exists="replace")
    print("✅ Data loaded into SQLite database!")

    # Step 3: Run SQL queries

    # Total spend by category
    query1 = """
    SELECT category, SUM(amount) AS total_spent
    FROM transactions
    GROUP BY category
    ORDER BY total_spent DESC
    """
    category_totals = pd.read_sql_query(query1, conn)
    print("\nTotal spend by category:")
    print(category_totals)

    # Customer-level spending stats
    query2 = """
    SELECT customer_id,
           COUNT(*) AS num_txns,
           AVG(amount) AS avg_spend,
           SUM(amount) AS total_spent
    FROM transactions
    GROUP BY customer_id
    """
    customer_stats = pd.read_sql_query(query2, conn)
    print("\nCustomer-level spending stats:")
    print(customer_stats)

    # Step 4: Visualize results

    # Bar chart: Total spend per category
    sns.barplot(data=category_totals, x="category", y="total_spent")
    plt.xticks(rotation=45)
    plt.title("Total Spend by Category")
    plt.ylabel("CAD")
    plt.tight_layout()
    plt.show()

    # Bar chart: Average spend per customer
    sns.barplot(data=customer_stats, x="customer_id", y="avg_spend")
    plt.title("Average Spend per Customer")
    plt.ylabel("CAD")
    plt.tight_layout()
    plt.show()

    conn.close()


if __name__ == "__main__":
    main()
