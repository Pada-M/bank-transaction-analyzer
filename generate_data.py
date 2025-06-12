# Cell 1 in analyzer.ipynb
from faker import Faker
import pandas as pd
import random

fake = Faker()
categories = [
    "Groceries",
    "Restaurants",
    "Utilities",
    "Travel",
    "Shopping",
    "Healthcare",
]
data = []

for _ in range(1000):
    data.append(
        {
            "customer_id": fake.random_int(min=1000, max=1010),
            "transaction_date": fake.date_between(start_date="-6M", end_date="today"),
            "amount": round(random.uniform(5, 500), 2),
            "merchant": fake.company(),
            "category": random.choice(categories),
        }
    )

df = pd.DataFrame(data)
df.to_csv("data/mock_transactions.csv", index=False)
