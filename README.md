# Assistente de Matchup – League of Legends (Projeto P0)
 
Este repositório contém a entrega do **Nível Básico** do Projeto P0 (Primeiro fluxo completo com LLM).
 
## 📌 Problema Escolhido
Durante a tela de carregamento de uma partida de League of Legends, os jogadores têm pouco tempo para entender como enfrentar o campeão inimigo da sua rota, e muitos não sabem quais são os pontos fortes e fracos de cada confronto.
 
## 🎯 Usuário ou Público
Jogadores iniciantes, casuais ou de elos iniciais (Ferro ao Ouro) que não conhecem todos os campeões do jogo.
 
## 🧠 Justificativa para Utilizar um LLM
O League of Legends possui mais de 160 campeões, resultando em dezenas de milhares de combinações possíveis de confrontos (matchups). Manter uma base de dados manual para todas elas seria inviável, e um LLM consegue gerar resumos táticos sob demanda para qualquer combinação.
 
## ⚙️ Funcionamento da Solução
A aplicação é um script Python executado localmente no terminal.
1. O sistema solicita três entradas do usuário: Campeão aliado, Campeão inimigo e Rota.
2. Os dados são inseridos em um *System Prompt* pré-formatado.
3. O script faz uma chamada via API para o modelo **Gemini 1.5 Flash** da Google.
4. O modelo retorna um resumo estrito em três tópicos estruturados, exibidos diretamente no terminal.
## 🚧 Limites do Projeto
Para respeitar o escopo da disciplina (P0), o projeto:
- Funciona exclusivamente via terminal (texto);
- Não possui interface web, gráfica ou mobile;
- Não possui banco de dados, RAG, ou múltiplos agentes;
- Realiza a chamada a apenas um único provedor de LLM.
## 💻 Instalação
 
1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```
 
2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```
 
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
 
## 🔑 Configuração do Acesso ao LLM
O projeto utiliza a API do Google Gemini. Para configurar o acesso:
 
1. Obtenha uma chave no [Google AI Studio](https://aistudio.google.com/).
2. Crie um arquivo chamado `.env` na raiz do projeto, baseando-se no arquivo `.env.example`.
3. Adicione a sua chave no arquivo:
```env
GEMINI_API_KEY=AIzaSySuaChaveAqui...
```
 
*Aviso: As credenciais de acesso ficam isoladas e estão protegidas pelo `.gitignore`.*
 
## 🚀 Execução
Com o ambiente ativado e as dependências instaladas, execute:
 
```bash
python main.py
```
 
## 📝 Exemplos de Entrada e Saída
 
**Entrada no Terminal:**
 
```text
=== Coach de Matchup: League of Legends ===
Seu campeão: garen
Campeão inimigo: darius
Rota (Top, Mid, Jungle, ADC, Sup): top
```
 
**Saída Gerada:**
 
```text
Analisando a matchup... (Aguarde)
 
=== Resumo Tático ===
- Vantagem Inicial: Darius é mais forte nos primeiros níveis devido à sua passiva (Hemorragia) e ao dano de trocas curtas.
- Condição de Vitória: Faça trocas curtas com o Q (Acerto Decisivo) e recue. Só vá para trocas longas quando tiver vantagem de vida ou nível.
- Cuidado Máximo: Evite ser puxado pelo E (Apreender) e fuja da borda externa do Q (Acerto Decisivo), onde o dano é maior.
```
 
## 🧪 Testes
Nesta etapa básica, os testes são manuais e executados simulando entradas no terminal.
 
- **Teste de sucesso:** Fornecer os três inputs válidos e verificar se a API retorna a formatação correta.
- **Teste de falha (Input):** Enviar campos vazios para acionar a validação do programa (`Erro: Todos os campos precisam ser preenchidos.`).
- **Teste de falha (Autenticação):** Simulado removendo a chave do `.env` para observar o tratamento do erro 400 (API Key Inválida). *(No nível Intermediário/Avançado, serão introduzidos testes automatizados)*.
## ⚠️ Limitações Conhecidas
- O uso da biblioteca depreciada `google.generativeai` foi mantido provisoriamente por apresentar melhor estabilidade em ambientes locais Windows com o pacote `python-dotenv` em relação ao SDK mais recente (`google-genai`).
- Não há limite máximo de tokens configurado, visando evitar o corte abrupto das frases, o que significa que o LLM pode, ocasionalmente, se alongar um pouco mais que o desejado.
## 🎥 Link para o Vídeo
[Insira o link de demonstração da execução aqui]