import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Charger la clé API depuis le fichier .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Envoyer une requête à l'IA
reponse = client.chat.completions.create(
    model="gpt-4o", # Vous pouvez changer le modèle ici
    messages=[
        {"role": "system", "content": "Tu es un assistant utile et concis."},
        {"role": "user", "content": "Explique-moi le concept de l'API en une phrase."}
    ]
)

# 3. Afficher la réponse
print(reponse.choices[0].message.content)
