import os
from dotenv import load_dotenv
import google.generativeai as genai

# override=True garante que ele vai ler o .env atual, ignorando o cache do Windows
load_dotenv(override=True)

def main():
    print("=== Coach de Matchup: League of Legends ===")
    meu_campeao = input("Seu campeão: ")
    campeao_inimigo = input("Campeão inimigo: ")
    rota = input("Rota (Top, Mid, Jungle, ADC, Sup): ")

    if not meu_campeao or not campeao_inimigo or not rota:
        print("Erro: Todos os campos precisam ser preenchidos.")
        return

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Erro: Chave da API não encontrada. Configure o arquivo .env.")
        return

    # Configuração na biblioteca clássica (a mesma do seu outro projeto)
    genai.configure(api_key=api_key)

    # O modelo 1.5-flash é o mais rápido e estável para texto
    model = genai.GenerativeModel('gemini-3.5-flash')

    prompt = f"""
    Atue como um coach de League of Legends nível Desafiante.
    Faça uma análise tática rápida da seguinte matchup: {meu_campeao} (meu campeão) contra {campeao_inimigo} (inimigo) na rota {rota}.
    
    Responda estritamente em português, formatando EXATAMENTE com os 3 tópicos abaixo (sem texto antes ou depois):
    - Vantagem Inicial: (explique quem é mais forte nos primeiros níveis)
    - Condição de Vitória: (explique o que fazer para ganhar a rota)
    - Cuidado Máximo: (diga qual habilidade inimiga evitar)
    """

    print("\nAnalisando a matchup... (Aguarde)\n")
    
    try:
        response = model.generate_content(
            prompt,
            # Deixe apenas a temperatura, sem limitar os tokens de saída
            generation_config=genai.types.GenerationConfig(
                temperature=0.4
            )
        )
        print("=== Resumo Tático ===")
        print(response.text)
        
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o LLM: {e}")

if __name__ == "__main__":
    main()