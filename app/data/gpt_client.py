import requests

class GPTClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/responses"

    def generate_response(self, question, check):
        print("chave openai", self.api_key)
        return "Error: OpenAI API key is not set."

    prompt = f"""
Você é uma assistente climática. Responda em português, de forma curta, clara e útil.
Pergunta do usuário: {question}
Dados reais do clima:
Cidade: {check.cidade}
Descrição: {check.descricao}
Temperatura: {check.temperatura}°C
Sensação térmica: {check.sensacao_termica}°C
Mínima: {check.temp_min}°C
Máxima: {check.temp_max}°C
Umidade: {check.umidade}%
Pressão: {check.pressao} hPa
Vento: {check.velocidade_vento} m/s
"""
    headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    payload = {
            "model": "gpt-4.1-mini",
            "input": prompt
        }
resposta = requests.post(self.url, headers=headers, json=payload, timeout=20)
if resposta.status_code != 200:
    return f"Erro OpenAI {resposta.status_code}: {resposta.text}"

dados = resposta.json()
    return dados.get("output_text", f"Resposta sem output_text: {dados}")

    def _resposta_local(self, pergunta, consulta):
        temp = consulta.temperatura
        if temp <= 15:
            dica = "Leve casaco, porque a temperatura está baixa."
        elif temp <= 24:
            dica = "O clima está agradável, mas vale levar uma blusa leve."
        else:
            dica = "Está quente, então use roupas leves e se hidrate bem."
        return(
            f"Em {consulta.cidade}, agora está {temp:.1f}°C, com sensação de "
            f"{consulta.sensacao_termica:.1f}°C e clima {consulta.descricao}. {dica}"
            )