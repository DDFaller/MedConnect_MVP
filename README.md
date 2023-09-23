

# MedConnect - API

Compartilhe seus estudos e aprenda com outras pessoas.

**MedConnect** tem como objetivo conectar a pessoas as clínicas médicas, facilitando e agilizando agendamentos.

Projeto desenvolvido para o MVP na Sprint 1 da Pós Graduação de Engenharia de Software da PUC-Rio.

> ⚠️ Para a utilização dessa API em uma aplicação front-end, você pode acessar o repositório da App desse projeto [clicando aqui](https://github.com/DDFaller/MedConnect_MVP).

## Executando a API


### 1 - Clonando o repositório

```
git clone https://github.com/DDFaller/Medconnect_MVP.git
```

#

Para executar a aplicação é necessário ter todas as libs (bibliotecas) python listadas no arquivo `requirements.txt` instaladas. 

#

### 2 - Criando um ambiente virtual (opcional)
s.

Você pode criar um  ambiente virtual a partir do seguinte comando:

```
python -m venv env
```

Após criar o ambiente virtual, você pode ativá-lo a partir do seguinte comando:

```
# Windows:
.\env\Scripts\activate.ps1

# Linux ou Mac:
source ./python_env/bin/activate
```

> ⚠️ Esse é um passo opcional, mas fortemente recomendável.

### 3 - Instalando as dependências


```
pip install -r requirements.txt
```
### 4 - Executando a API
Finalmente, para executar a API, basta executar o seguinte comando:

```
(env)$ flask run 
```

Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte, conforme abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

### 5 - Carregando dados iniciais no Banco de Dados
Para carregar dados iniciais no banco de dados, execute o seguinte comando:

```
(env)$ python load_db.py
```

Ao final, cole esse endereço no seu navegador para visualizar a documentação da API e suas rotas:

```
localhost:5000
```


