# import json
# from faker import Faker
#
# # Initialize Faker
# fake = Faker()
#
# # Generate JSON data for news
# num_records = 50000  # Adjust as needed
# news_data = []
#
# for _ in range(num_records):
#     news_item = {
#         'title': fake.sentence(nb_words=6, variable_nb_words=True)[:100],  # News headline
#         'content': ' '.join(fake.paragraphs(nb=3))[:1000]  # Article body
#     }
#     news_data.append(news_item)
#
# # Save to JSON file
# with open('news_data.json', 'w') as f:
#     json.dump(news_data, f, indent=4)
#
# print(f"Generated {num_records} news items in news_data.json")

# import json
# import random
# from faker import Faker
#
# # Initialize Faker
# fake = Faker()
#
# # Define car type mapping
# TYPE_CHOICES = {
#     1: 'Ford',
#     2: 'BMW',
#     3: 'Mercedes'
# }
#
# # Number of records to generate
# num_records = 50000
#
# car_data = []
#
# for _ in range(num_records):
#     car_type = random.choice(list(TYPE_CHOICES.keys()))
#     car = {
#         'name': fake.company()[:100],
#         'price': random.randint(10000, 100000),
#         'type': car_type,
#         'type_string': TYPE_CHOICES[car_type]  # Optional: for readability
#     }
#     car_data.append(car)
#
# # Save to JSON file
# with open('car_data.json', 'w') as f:
#     json.dump(car_data, f, indent=4)
#
# print(f"Generated {num_records} car records in car_data.json")


import json
from faker import Faker
import random

fake = Faker()

CATEGORY_CHOICES = ['Beauty', 'Home', 'Sanitation', 'daily needs']

# Number of products to generate
NUM_PRODUCTS = 50000

products = []

for _ in range(NUM_PRODUCTS):
    product = {
        "name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "price": random.randint(50, 1000),
        "category": random.choice(CATEGORY_CHOICES)
    }
    products.append(product)

# Save to JSON file
with open("fake_products.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Generated {NUM_PRODUCTS} fake products in 'fake_products.json'")
