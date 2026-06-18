# PyTaco API

Uma API RESTful para consulta de macronutrientes baseada na **Tabela Brasileira de Composição de Alimentos (TACO)**, mantida pela Unicamp.

O projeto foi desenvolvido em Python e estruturado com base nos princípios de **Clean Architecture** e **SOLID**, separando rigorosamente o pipeline de extração de dados (ETL) da camada de entrega HTTP.

## Estrutura do Projeto

Para garantir o **Princípio da Responsabilidade Única (SRP)** e isolar falhas, o repositório é dividido em duas aplicações independentes:

* **`data_pipeline/`**: Script executado sob demanda para ler a planilha bruta da Unicamp (Excel), higienizar marcadores textuais, agrupar os alimentos e gerar um banco de dados estático (`taco_macros.json`). Construído com `pandas`.
* **`api/`**: A camada web servida via **FastAPI**. Carrega o JSON estruturado diretamente para a memória RAM no momento da inicialização (garantindo latência mínima). Utiliza padrões **DTO** via Pydantic para traduzir as chaves do banco de dados para `camelCase`, facilitando o consumo por aplicações *frontend*.

## Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** + **Uvicorn** (Servidor ASGI)
* **Pydantic V2** (Validação de contratos de dados)
* **Pandas** (Exclusivo para o ambiente de Data Pipeline)

## Como Executar a API Localmente

Graças à separação de contextos, o desenvolvedor não precisa rodar ou possuir dependências de engenharia de dados (como Pandas) para iniciar a API. O artefato JSON já está disponível na pasta `data`.

**1. Clone o repositório e acesse a pasta da API:**
```bash
git clone [https://github.com/seu-usuario/PyTacoAPI.git](https://github.com/seu-usuario/PyTacoAPI.git)
cd PyTacoAPI/api

```

**2. Crie e ative o ambiente virtual:**

```bash
python -m venv .venv

# No Windows:
.venv\Scripts\activate
# No Linux/macOS:
source .venv/bin/activate

```

**3. Instale as dependências da camada web:**

```bash
pip install -r requirements.txt

```

**4. Inicie o servidor:**

```bash
uvicorn src.main:app --reload

```

O servidor estará disponível localmente em `http://127.0.0.1:8000`.

## Documentação Interativa (Swagger)

O FastAPI gera automaticamente a especificação OpenAPI baseada na tipagem forte do código. Com o servidor em execução, acesse a interface gráfica pelo navegador para testar as rotas:

* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

## Endpoints Disponíveis

* `GET /api/v1/food` - Retorna todos os alimentos catalogados na TACO, agrupados hierarquicamente por suas respectivas categorias.
* `GET /api/v1/food/category` - Retorna a lista dos nomes das categorias de alimentos disponíveis.
* `GET /api/v1/food/{food_id}` - Retorna os macronutrientes detalhados (proteínas, lipídios, carboidratos, calorias) de um alimento específico a partir de seu ID.

```
