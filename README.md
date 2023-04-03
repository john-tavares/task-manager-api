# Task Manager API
Este projeto é uma API para gerenciamento de tarefas (tasks), onde é possível criar, editar e deletar tarefas, bem como marcá-las como concluídas ou não.

## Utilização
Para utilizar a API, é necessário ter o Python 3.6 ou superior instalado em sua máquina. Além disso, é recomendado o uso de um ambiente virtual, como o virtualenv.

Para instalar as dependências do projeto, execute o comando:

```
pip install -r requirements.txt
```

Para criar o banco de dados e executar as migrações, execute os comandos:

```
flask db init
flask db migrate
flask db upgrade
```

Para rodar a aplicação, execute o comando:
```
flask run
```

Após a execução do comando acima, a API estará rodando em http://localhost:5000.

## Testes
Para testar a API, é possível utilizar o arquivo [Task Manager - Postman Collection](docs/task-manager-api.postman_collection), que se encontra na pasta `docs` do projeto. Esse arquivo contém exemplos de requisições para todas as rotas da API.

## Rotas
A API possui as seguintes rotas:

### GET /tasks
Retorna todas as tarefas cadastradas.

### POST /tasks
Cria uma nova tarefa.

Exemplo de corpo da requisição:
```
{
    "title": "Título da tarefa",
    "description": "Descrição da tarefa"
}
```
### GET /tasks/<int:task_id>
Retorna os detalhes de uma tarefa específica.

### PUT /tasks/<int:task_id>
Atualiza os detalhes de uma tarefa específica.

Exemplo de corpo da requisição:

```
{
    "title": "Novo título da tarefa",
    "description": "Nova descrição da tarefa",
    "done": true
}
```
### DELETE /tasks/<int:task_id>
Deleta uma tarefa específica.
