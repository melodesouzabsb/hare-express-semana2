from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

modelo = "gemini-1.5-flash"
cliente = genai.GenerativeModel(model_name = modelo)

prompt = "Elenque 10 dias para iniciar na programação em Python."
resposta = cliente.generate_content(prompt)
print(resposta.text)