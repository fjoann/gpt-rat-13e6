import json
import openai
import os
import requests

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Load the list of companies from the .json file
with open("companies.json", "r") as f:
    companies = json.load(f)

# Make a call to the GPT-3 API for each company
for company in companies:
    print(f"Generating description for {company['name']} ({companies.index(company) + 1} / {len(companies)}).")
    # Define the prompt
    prompt = (f"Describe the company {company['name']} which operates in the {company['industry']} industry and is {company['size']} in size in two short paragraphs.")
    
    # Make the API call
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = """
    {
        """
    data += f'"prompt": "{prompt}",'
    data += """
        "model": "text-davinci-003",
        "max_tokens": 200
    }
    """
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, data=data)
    company_description = response.json()['choices'][0]['text']
    company["description"] = company_description

# Write the list of companies with descriptions to a .json file
with open("companies_with_descriptions.json", "w") as f:
    json.dump(companies, f)
