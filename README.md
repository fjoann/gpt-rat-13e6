### How to use

NOTE: These instructions were tested on Ubuntu in WSL2.

Get an API key from you OpenAI account (https://beta.openai.com/account/api-keys).

Add the API key to your environment as `OPENAI_API_KEY`.

```
export OPENAI_API_KEY=...
```

Create and activate a virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements.

```
pip install -r requirements.txt
```

Run the scripts.

```
python3 generate-companies.py
python3 get-descriptions.py
```
