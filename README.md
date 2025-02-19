# Sistema Financeiro Pessoal

<img src="https://socialify.git.ci/fabricioifc/bizofin-new/image?description=1&amp;descriptionEditable=Projeto%20Acad%C3%AAmico&amp;forks=1&amp;language=1&amp;name=1&amp;pattern=Plus&amp;stargazers=1&amp;theme=Light" alt="project-image">

Bizofin é uma plataforma de gestão financeira voltada para pessoas físicas. A nova versão, chamada de "Bizofin New", foi desenvolvida com propósitos edutativos apenas.

O projeto foi desenvolvido para a disciplina de Desenvolvimento Web.

<img src="https://img.shields.io/pypi/l/pip" alt="shields">

----------

## Enunciado do Exercício Prático
O objetivo deste exercício prático é desenvolver um sistema financeiro pessoal simples usando Flask, SQLite e Heroku.

O sistema deve permitir que os usuários adicionem, atualizem e excluam suas despesas e receitas. Cada transação deve ter uma conta, uma descrição, um valor e uma data.

Para implementar o sistema, siga os seguintes passos:

* Crie uma estrutura básica de aplicativo Flask. Configure o Flask para usar SQLite como banco de dados.
* Crie uma tabela "transacoes ou lançamentos" no banco de dados SQLite. A tabela deve ter colunas para conta, descrição, valor, data e status.
* Implemente as rotas do aplicativo Flask para permitir que os usuários adicionem, atualizem e excluam transações.
* Crie modelos de formulário para permitir que os usuários adicionem e atualizem contas e transações.
* Adicione a funcionalidade de autenticação em seu aplicativo Flask para permitir que apenas usuários registrados acessem o sistema.
* Adicione a funcionalidade de sessão em seu aplicativo Flask para permitir que os usuários permaneçam conectados após o login.
* Implemente uma página de resumo que mostre o total de despesas e receitas do usuário.
* Implante o aplicativo Flask em um servidor Heroku. Configure o Heroku para usar MySQL como banco de dados.
* Crie alguns testes unitários para o aplicativo Flask usando pytest.
* Verifique se seu aplicativo está funcionando corretamente no Heroku.

Ao concluir este exercício prático, você terá aprendido habilidades importantes de desenvolvimento web, como a criação de rotas, o uso de bancos de dados, o desenvolvimento de modelos de formulário, a implementação de autenticação de usuários e a implantação de aplicativos na nuvem. Você também terá desenvolvido um sistema financeiro pessoal útil para gerenciar suas finanças.

----------
## 🚀 Demo

O projeto está disponível para acesso no seguinte link:

[http://bizofin.herokuapp.com/](http://bizofin.herokuapp.com/)

## Tela do Projeto

<img src="https://api.pikwy.com/web/642ad54180f62963e04e5eaa.jpg" alt="project-screenshot" width="480" height="320/">
 
## 🧐 Funcionalidades

Algumas das funcionalidades incluem:

* Cadastro de usuário
* Login de usuário
* Recuperação de senha
* Autorização de acesso para rotas
* Cadastro de contas
* Lançamento de receitas e despesas
* Dashboard com o saldo atual de cada conta

## Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [] Adicionar a coluna categoria na tabela de transações
- [] Permitir a transferência de valores entre contas
- [] Criar filtros para as transações

## 📝 Documentação
###### em construção

A documentação do projeto está disponível no seguinte link:

[https://bizofin.herokuapp.com/docs](https://bizofin.herokuapp.com/docs)

## 🛠️ Como rodar o projeto:

Para rodar o projeto localmente, siga os passos abaixo:

1. Antes de começar, é necessário ter instalado em sua máquina: 
 - `Python 3.10.8` ou superior
 - `PIP 23.0.1` ou superior
 - `GIT 2.33.1` ou superior
 - `Visual Studio Code` (ou outro editor de código)

2. Clonar o projeto

```
git clone https://github.com/fabricioifc/bizofin-new.git
```

3. Criar um ambiente virtual

```
python -m venv .venv
```

4. Instalar as bibliotecas requeridas

```
python -m pip install -r requirementx.txt
```

5. Configurando o ambiente

```
cp .flaskenv.example .flaskenv
```
Alterar as variáveis de ambiente no arquivo `.flaskenv` de acordo com o seu ambiente.
```	
FLASK_APP=app
FLASK_DEBUG=True
FLASK_RUN_PORT=5000
FLASK_RUN_HOST=0.0.0.0
SECRET_KEY=**************************
CONFIG_TYPE=config.DevelopmentConfig
```	

Para gerar uma SECRET_KEY, basta rodar o seguinte comando no terminal:

```
python -c 'import uuid; print(uuid.uuid4().hex)'
```

Caso queira rodar o projeto em modo produção na plataforma Heroku, é necessário adicionar as seguintes variáveis de ambiente no arquivo `.flaskenv`:

```	
JAWSDB_MARIA_URL=mysql+pymysql://USUARIO:SENHA@URL:3306/DATABASE_NAME
MAILGUN_SMTP_SERVER=smtp.mailgun.org
MAILGUN_SMTP_PORT=587
MAILGUN_SMTP_LOGIN=URL_GERADA_PELA_EXTENSAO
MAILGUN_SMTP_PASSWORD=SENHA_GERADA_PELA_EXTENSAO
```	

As dependências ``JAWSDB`` e ``MAILGUN`` são necessárias para o funcionamento correto do projeto em produção. Podem ser adicionadas no  painel de configurações da plataforma ``Heroku``.

6. Rodar o projeto em modo desenvolvimento</p>

```
python -m flask run
```

7. Acessar o projeto em seu navegador

`http://localhost:5000/`

8. (opcional) Deploy da aplicação

Para fazer o deploy da aplicação, é necessário ter uma conta no Heroku e instalar o Heroku CLI em sua máquina. Para mais informações, acesse a documentação oficial do Heroku: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

```
heroku login
heroku create
git push heroku main
```
  
## 💻 Desenvolvido com

Principais bibliotecas utilizadas no projeto:

*   Bootstrap-Flask v2.2.0
*   Flask v2.2.3
*   flask-babel v3.0.1
*   Flask-Bcrypt v1.0.1
*   Flask-Breadcrumbs v0.5.1
*   Flask-Login v0.6.2
*   Flask-Mail v0.9.1
*   Flask-Menu v0.7.2
*   Flask-Migrate v4.0.4
*   Flask-SQLAlchemy v3.0.3
*   Flask-WTF v1.1.1
*   gunicorn v20.1.0 (production only)
*   Jinja2 v3.1.2
*   pytest v7.2.2
*   python-dotenv v1.0.0
*   SQLAlchemy v2.0.7

## 🍰 Como contribuir

Caso queira contribuir com o projeto sinta-se à vontade para abrir uma issue ou enviar um ``pull request``.

## 🛡️ Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

## 📧 Contato

![GitHub language count](https://img.shields.io/github/languages/count/fabricioifc/README-template?style=for-the-badge)

Fabricio Bizotto
[https://www.linkedin.com/in/fabricio-bizotto/](https://www.linkedin.com/in/fabricio-bizotto/)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com{:target="_blank"})

[⬆ Voltar ao topo](#nome-do-projeto)<br>