# Pipeline de Dados Simples — Python, Docker e Terraform

Projeto desenvolvido como um **laboratório prático de Engenharia de Dados e Infraestrutura como Código (IaC)**.

A ideia inicial é simples: criar dados utilizando Python e Pandas, salvar esses dados em um arquivo `.txt` e posteriormente transformá-los em `.csv`.

A partir desse fluxo básico, o projeto evolui gradualmente para:

```text
Python + POO
     ↓
Poetry
     ↓
Docker
     ↓
Terraform
     ↓
Terraform gerenciando Docker
```

O objetivo principal deste laboratório não é construir uma pipeline complexa, mas **entender os fundamentos por trás de cada tecnologia e como elas se conectam**.

---

# 1. Objetivo do Projeto

O projeto simula uma pequena pipeline de dados:

```text
Geração dos dados
       ↓
DataFrame Pandas
       ↓
Arquivo TXT
       ↓
Leitura do TXT
       ↓
DataFrame Pandas
       ↓
Arquivo CSV
```

O fluxo é executado inicialmente de forma local e posteriormente empacotado em um container Docker.

Por fim, utilizamos Terraform para praticar **Infrastructure as Code (IaC)** e gerenciar os recursos Docker.

---

# 2. O que foi aprendido

Durante a construção deste laboratório foram praticados os seguintes conceitos:

### Python

* Programação Orientada a Objetos (POO)
* Classes
* Métodos
* Construtor `__init__`
* Importação de classes entre arquivos
* Manipulação de arquivos
* Pandas
* DataFrames
* Geração de CSV

### Poetry

* Gerenciamento de dependências
* `pyproject.toml`
* `poetry.lock`
* Ambientes virtuais
* Instalação das dependências
* Reprodutibilidade do ambiente

### Docker

* Dockerfile
* Imagens
* Containers
* `docker build`
* `docker run`
* Volumes
* Logs
* Parada e remoção de containers
* Remoção de imagens

### Terraform

* Infrastructure as Code
* Providers
* Resources
* `terraform init`
* `terraform validate`
* `terraform plan`
* `terraform apply`
* Terraform State
* Dependência entre recursos
* Provider Docker
* Gerenciamento de uma imagem Docker através do Terraform
* Gerenciamento de um container Docker através do Terraform

---

# 3. Arquitetura do Laboratório

A arquitetura final do laboratório é:

```text
                         TERRAFORM
                             │
                             ▼
                    Docker Provider
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       Docker Image                  Docker Container
       pipeline-csv:1.0                  pipeline-csv
              │                             │
              │                             ▼
              │                         main.py
              │                             │
              │                  ┌──────────┴──────────┐
              │                  ▼                     ▼
              │             output.txt            output.csv
              │
              ▼
       Python 3.12
       Poetry
       Pandas
       Aplicação
```

---

# 4. Estrutura do Projeto

```text
project_data/
│
├── entrada/
│   └── output.txt
│
├── saida/
│   └── output.csv
│
├── create_file_txt.py
├── transform_txt_in_csv.py
├── main.py
│
├── Dockerfile.fn_run_pipeline_csv
│
├── pyproject.toml
├── poetry.lock
├── README.md
│
└── terraform/
    ├── main.tf
    ├── .terraform/
    ├── .terraform.lock.hcl
    └── terraform.tfstate
```

> `.terraform/` e `terraform.tfstate` são arquivos gerados pelo Terraform e devem ser tratados de acordo com a estratégia de versionamento escolhida para o projeto.

---

# 5. Etapa 1 — Desenvolvimento da Pipeline em Python

Antes de utilizar Docker ou Terraform, a aplicação foi desenvolvida e testada localmente.

A primeira etapa foi criar uma classe responsável por gerar um DataFrame utilizando Pandas.

Exemplo conceitual:

```python
import pandas as pd

class CreateDataFrame:

    def __init__(self):
        self.df = None

    def create_dataframe(self):

        data = {
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Age": [25, 30, 35, 40],
            "City": [
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston"
            ]
        }

        self.df = pd.DataFrame(data)

        return self.df
```

O objetivo aqui foi praticar POO e entender como uma classe pode encapsular a criação e manipulação de um DataFrame.

---

# 6. Etapa 2 — Criação do Arquivo TXT

Depois da criação do DataFrame, foi criado um método responsável por salvar os dados em arquivo.

O fluxo ficou:

```text
CreateDataFrame
       ↓
create_dataframe()
       ↓
Pandas DataFrame
       ↓
save_to_csv()
       ↓
entrada/output.txt
```

Apesar do método utilizar recursos do Pandas, o objetivo do laboratório foi justamente experimentar o fluxo de geração e transformação de arquivos.

---

# 7. Etapa 3 — Transformação TXT → CSV

Foi criada uma segunda classe para realizar a transformação:

```text
entrada/output.txt
       ↓
Pandas
       ↓
DataFrame
       ↓
saida/output.csv
```

Exemplo:

```python
import pandas as pd

class TransformTxtToCsv:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def transform(self):

        df = pd.read_csv(
            self.input_file,
            delimiter=","
        )

        df.to_csv(
            self.output_file,
            index=False
        )
```

---

# 8. Etapa 4 — Orquestração com `main.py`

Depois criamos um arquivo principal responsável por chamar as etapas da pipeline.

A ideia é centralizar a execução:

```text
main.py
   │
   ├── Criação dos dados
   │
   └── Transformação TXT → CSV
```

Isso permitiu separar responsabilidades entre os arquivos.

---

# 9. Etapa 5 — Poetry

Depois de testar o código Python, utilizamos o Poetry para gerenciar as dependências.

## Instalação

No Ubuntu/WSL:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Depois valide:

```bash
poetry --version
```

Exemplo:

```text
Poetry (version 2.4.1)
```

---

# 10. Instalação das Dependências

Dentro do projeto:

```bash
cd project_data
```

Execute:

```bash
poetry install
```

O Poetry utiliza:

```text
pyproject.toml
```

para definir as dependências e:

```text
poetry.lock
```

para garantir versões reprodutíveis.

---

# 11. Verificação do Projeto

Podemos verificar a configuração utilizando:

```bash
poetry check
```

Durante o desenvolvimento foram encontradas mensagens relacionadas ao formato mais moderno do `pyproject.toml`, como:

```text
[tool.poetry.name] is deprecated.
[tool.poetry.version] is deprecated.
[tool.poetry.description] is deprecated.
```

Essas mensagens são warnings relacionados à evolução da especificação do Poetry.

O ponto importante é diferenciar:

```text
Warning
```

de:

```text
Error
```

Um warning não necessariamente impede a execução do projeto.

---

# 12. Execução Local

Com as dependências instaladas:

```bash
poetry run python main.py
```

ou, caso o ambiente virtual esteja ativado:

```bash
python main.py
```

A aplicação deve gerar:

```text
entrada/output.txt
```

e:

```text
saida/output.csv
```

---

# 13. Etapa 6 — Docker

Depois de validar a aplicação localmente, passamos para Docker.

O objetivo foi empacotar:

```text
Python
Poetry
Pandas
Código da aplicação
```

dentro de uma imagem.

---

# 14. Dockerfile

O projeto utiliza:

```text
Dockerfile.fn_run_pipeline_csv
```

A imagem utiliza Python 3.12:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry==2.4.1

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-interaction --no-ansi

COPY create_file_txt.py .
COPY transform_txt_in_csv.py .
COPY main.py .

RUN mkdir -p /app/entrada /app/saida

CMD ["python", "main.py"]
```

---

# 15. Construindo a Imagem Docker

Dentro do diretório do projeto:

```bash
docker build \
  -f Dockerfile.fn_run_pipeline_csv \
  -t pipeline-csv:1.0 .
```

Ou em uma única linha:

```bash
docker build -f Dockerfile.fn_run_pipeline_csv -t pipeline-csv:1.0 .
```

Exemplo de resultado:

```text
[+] Building ... FINISHED
...
=> naming to docker.io/library/pipeline-csv:1.0
```

Podemos verificar:

```bash
docker images | grep pipeline
```

Resultado:

```text
pipeline-csv:1.0
```

---

# 16. Conceito Importante: Imagem ≠ Container

Um dos principais conceitos aprendidos neste laboratório:

```text
IMAGE
  ↓
é o molde

CONTAINER
  ↓
é uma instância executável da imagem
```

Quando executamos:

```bash
docker build
```

criamos uma **imagem**.

Quando executamos:

```bash
docker run
```

criamos e iniciamos um **container** baseado nessa imagem.

Portanto:

```text
Dockerfile
    ↓
docker build
    ↓
pipeline-csv:1.0
    ↓
docker run
    ↓
pipeline-csv
    ↓
main.py
```

---

# 17. Executando o Container

Para executar a imagem:

```bash
docker run --name pipeline-csv \
  -v "$(pwd)/entrada:/app/entrada" \
  -v "$(pwd)/saida:/app/saida" \
  pipeline-csv:1.0
```

Os volumes fazem o mapeamento:

```text
máquina local              container

entrada/       ←→          /app/entrada
saida/         ←→          /app/saida
```

Isso permite que os arquivos gerados pelo container permaneçam disponíveis no ambiente local.

---

# 18. Verificando Containers

Para visualizar containers em execução:

```bash
docker ps
```

Para visualizar todos os containers:

```bash
docker ps -a
```

Exemplo:

```text
CONTAINER ID   IMAGE             STATUS
1c1dc60d0fe4   pipeline-csv:1.0  Exited (0)
```

`Exited (0)` indica que o processo terminou com código de saída `0`, normalmente significando execução bem-sucedida.

---

# 19. Visualizando Logs

Para visualizar os logs:

```bash
docker logs pipeline-csv
```

Para acompanhar os logs:

```bash
docker logs -f pipeline-csv
```

Os `print()` existentes no Python aparecem nos logs do container.

Isso permite verificar se:

```text
container
   ↓
main.py
   ↓
pipeline executada
```

---

# 20. Parando um Container

Para parar um container em execução:

```bash
docker stop pipeline-csv
```

Verifique:

```bash
docker ps -a
```

---

# 21. Removendo um Container

Para remover:

```bash
docker rm pipeline-csv
```

Se o container estiver em execução:

```bash
docker stop pipeline-csv
docker rm pipeline-csv
```

---

# 22. Removendo Imagens

Para visualizar as imagens:

```bash
docker images
```

Para remover a imagem:

```bash
docker rmi pipeline-csv:1.0
```

Caso existam containers utilizando a imagem, eles precisam ser removidos antes.

---

# 23. Limpeza de Containers Antigos

Para remover containers parados:

```bash
docker container prune
```

O Docker solicitará confirmação.

Para visualizar antes:

```bash
docker ps -a
```

> Use comandos de limpeza com atenção em ambientes que contenham containers importantes.

---

# 24. Etapa 7 — Terraform

Depois de entender:

```text
Python
  ↓
Poetry
  ↓
Docker
```

iniciamos a etapa de **Infrastructure as Code**.

O objetivo foi utilizar Terraform para gerenciar a infraestrutura Docker localmente.

Nenhuma AWS, GCP, Azure ou outra cloud é necessária.

Tudo acontece localmente.

---

# 25. Terraform + Docker

O Terraform utiliza um provider para conversar com o Docker.

O provider utilizado foi:

```text
kreuzwerker/docker
```

Configuração:

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}
```

O socket:

```text
/var/run/docker.sock
```

permite que o Terraform se comunique com o Docker local.

---

# 26. Inicializando o Terraform

Dentro do diretório Terraform:

```bash
terraform init
```

Exemplo:

```text
Initializing the backend...
Initializing provider plugins...

Terraform has been successfully initialized!
```

Durante esse processo, o Terraform instala o provider Docker.

Também é criado:

```text
.terraform.lock.hcl
```

Esse arquivo registra a versão selecionada do provider.

---

# 27. Terraform Validate

Para verificar se a configuração está válida:

```bash
terraform validate
```

Resultado esperado:

```text
Success! The configuration is valid.
```

---

# 28. Primeiro Resource Terraform

O primeiro recurso criado foi a imagem Docker:

```hcl
resource "docker_image" "pipeline" {
  name = "pipeline-csv:1.0"
}
```

Aqui começamos a utilizar um conceito fundamental do Terraform:

```text
resource
```

Um resource representa algo que o Terraform irá gerenciar.

Nesse caso:

```text
docker_image.pipeline
```

representa a imagem Docker.

---

# 29. Terraform Plan

Antes de criar ou alterar infraestrutura:

```bash
terraform plan
```

Exemplo:

```text
Terraform will perform the following actions:

# docker_image.pipeline will be created
+ resource "docker_image" "pipeline" {
    + id          = (known after apply)
    + image_id    = (known after apply)
    + name        = "pipeline-csv:1.0"
}

Plan: 1 to add, 0 to change, 0 to destroy.
```

O `plan` é uma etapa extremamente importante.

Ele permite visualizar:

```text
O que será criado?
O que será alterado?
O que será destruído?
```

antes da execução.

---

# 30. Terraform Apply

Depois de validar o plano:

```bash
terraform apply
```

O Terraform solicita confirmação:

```text
Do you want to perform these actions?

Only 'yes' will be accepted.
```

Digitamos:

```text
yes
```

Resultado:

```text
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Nesse momento o Terraform passou a gerenciar a imagem Docker.

---

# 31. Terraform State

Podemos verificar os recursos atualmente gerenciados:

```bash
terraform state list
```

Resultado esperado:

```text
docker_image.pipeline
```

O Terraform mantém informações sobre os recursos no:

```text
terraform.tfstate
```

O State é fundamental porque permite ao Terraform saber qual infraestrutura ele está gerenciando.

---

# 32. Imagem Docker Gerenciada pelo Terraform

Depois do primeiro `apply`, tivemos:

```text
Terraform
    ↓
docker_image.pipeline
    ↓
pipeline-csv:1.0
```

A imagem passou a fazer parte do estado do Terraform.

---

# 33. Criando o Container com Terraform

Depois de criar e entender a imagem, adicionamos um segundo recurso:

```hcl
resource "docker_container" "pipeline" {
  name  = "pipeline-csv"
  image = docker_image.pipeline.image_id
}
```

Aqui existe uma relação entre os recursos:

```text
docker_image.pipeline
        │
        │ image_id
        ▼
docker_container.pipeline
```

O Terraform consegue identificar essa dependência automaticamente.

---

# 34. Conceito Importante: Dependência entre Resources

Quando escrevemos:

```hcl
image = docker_image.pipeline.image_id
```

estamos dizendo:

> O container utiliza a imagem criada pelo recurso `docker_image.pipeline`.

Assim:

```text
1. docker_image.pipeline
          ↓
2. docker_container.pipeline
```

O Terraform entende que a imagem precisa existir antes que o container seja criado.

---

# 35. Segundo Terraform Plan

Depois de adicionar o container:

```bash
terraform plan
```

O Terraform identificou:

```text
docker_image.pipeline
```

como existente e:

```text
docker_container.pipeline
```

como novo recurso.

Resultado:

```text
Plan: 1 to add, 0 to change, 0 to destroy.
```

Isso demonstra um dos principais conceitos do Terraform:

> O Terraform não simplesmente executa comandos novamente. Ele compara o estado desejado com o estado atual e determina quais ações são necessárias.

---

# 36. Fluxo Final

O laboratório evoluiu da seguinte maneira:

```text
┌─────────────────────────────┐
│         PYTHON              │
│                             │
│ Classes + Pandas + POO      │
└──────────────┬──────────────┘
               │
               ▼
        main.py executa
               │
               ▼
       output.txt / output.csv
               │
               ▼
┌─────────────────────────────┐
│           POETRY            │
│                             │
│ Dependências + Lock         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│           DOCKER            │
│                             │
│ Dockerfile                  │
│       ↓                     │
│ Docker Image                │
│       ↓                     │
│ Docker Container            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          TERRAFORM          │
│                             │
│ Provider Docker             │
│       ↓                     │
│ docker_image                │
│       ↓                     │
│ docker_container             │
└─────────────────────────────┘
```

---

# 37. Comandos Principais do Laboratório

## Python / Poetry

```bash
poetry --version
```

```bash
poetry install
```

```bash
poetry check
```

```bash
poetry run python main.py
```

---

## Docker

Construir imagem:

```bash
docker build -f Dockerfile.fn_run_pipeline_csv -t pipeline-csv:1.0 .
```

Listar imagens:

```bash
docker images
```

Executar container:

```bash
docker run --name pipeline-csv \
  -v "$(pwd)/entrada:/app/entrada" \
  -v "$(pwd)/saida:/app/saida" \
  pipeline-csv:1.0
```

Listar containers:

```bash
docker ps
```

```bash
docker ps -a
```

Visualizar logs:

```bash
docker logs pipeline-csv
```

Acompanhar logs:

```bash
docker logs -f pipeline-csv
```

Parar:

```bash
docker stop pipeline-csv
```

Remover container:

```bash
docker rm pipeline-csv
```

Remover imagem:

```bash
docker rmi pipeline-csv:1.0
```

---

## Terraform

Inicializar:

```bash
terraform init
```

Formatar:

```bash
terraform fmt
```

Validar:

```bash
terraform validate
```

Visualizar plano:

```bash
terraform plan
```

Aplicar:

```bash
terraform apply
```

Visualizar recursos no State:

```bash
terraform state list
```

Visualizar o State:

```bash
terraform show
```

Destruir recursos gerenciados pelo Terraform:

```bash
terraform destroy
```

---

# 38. Próximos Passos

Este projeto foi construído propositalmente de forma incremental.

Possíveis evoluções:

```text
Pipeline Python
      ↓
Docker
      ↓
Terraform
      ↓
Docker Compose
      ↓
PostgreSQL
      ↓
Airflow
      ↓
Orquestração
      ↓
Testes automatizados
      ↓
CI/CD
```

Também podem ser explorados posteriormente:

* Terraform Modules
* Variables
* Outputs
* `terraform.tfvars`
* Remote State
* Docker Networks
* PostgreSQL
* Airflow
* Observabilidade
* Testes com Pytest
* CI/CD com GitLab
* Estruturação de ambientes `dev`, `staging` e `prod`

---

# 39. Conclusão

Este laboratório demonstra como uma aplicação extremamente simples pode ser utilizada para compreender conceitos fundamentais de Engenharia de Dados e Infraestrutura.

Começamos com uma aplicação Python utilizando POO e Pandas:

```text
Python
```

Depois adicionamos gerenciamento de dependências:

```text
Python + Poetry
```

Em seguida empacotamos a aplicação:

```text
Python + Poetry + Docker
```

E finalmente adicionamos Infrastructure as Code:

```text
Python
   +
Poetry
   +
Docker
   +
Terraform
```

O principal aprendizado é entender a responsabilidade de cada camada:

```text
Python
→ lógica da aplicação

Poetry
→ dependências

Docker
→ empacotamento e execução

Terraform
→ gerenciamento da infraestrutura
```

Tudo isso pode ser executado **localmente**, sem necessidade de provisionar recursos em cloud e sem gerar custos de infraestrutura.

---

# Autor

Laboratório desenvolvido como projeto de estudos práticos em:

* Engenharia de Dados
* Python
* Docker
* Infrastructure as Code
* Terraform
* DevOps

O projeto será evoluído gradualmente, adicionando novas camadas de infraestrutura e processamento de dados conforme os conceitos forem aprendidos.
