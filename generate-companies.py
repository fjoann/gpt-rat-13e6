import random
import json

from faker import Faker

# Create a list of company names
faker = Faker()
company_names = []
for i in range(100):
    company_names.append(faker.company())

# Create a list of industries, and sizes
industries = ["Technology", "Finance", "Retail"]
sizes = ["Small", "Medium", "Large"]

# Generate a list of companies with random names, industries, and sizes
companies = []
for i in range(100):
    company = {}
    company["name"] = random.choice(company_names)
    company["industry"] = random.choice(industries)
    company["size"] = random.choice(sizes)
    companies.append(company)

# Write the list of companies to a .json file
with open("companies.json", "w") as f:
    json.dump(companies, f)
