<h1 align="center" id="title">Sistema Financeiro Pessoal</h1>

<p align="center"><img src="https://socialify.git.ci/fabricioifc/bizofin-new/image?description=1&amp;descriptionEditable=Projeto%20Acad%C3%AAmico&amp;forks=1&amp;language=1&amp;name=1&amp;pattern=Plus&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">
O Bizofin é uma plataforma de gestão financeira voltada para pessoas físicas. A nova versão, chamada de "Bizofin New", foi desenvolvida com propósitos edutativos apenas.

O projeto foi desenvolvido por FabricioIFC para a disciplina de Desenvolvimento Web.
</p>

<p align="center"><img src="https://img.shields.io/pypi/l/pip" alt="shields"><img src="https://img.shields.io/pypi/l/Flask-Bcrypt" alt="shields"></p>

<h2>🚀 Demo</h2>

[http://bizofin.herokuapp.com/](http://bizofin.herokuapp.com/)

<h2>Project Screenshots:</h2>

<img src="https://api.pikwy.com/web/642ad54180f62963e04e5eaa.jpg" alt="project-screenshot" width="1280" height="1024/">

  
<h2>🧐 Funcionalidades</h2>

Algumas das funcionalidades incluem:

* Cadastro de usuário
* Login de usuário
* Cadastro de contas
* Lançamento de receitas e despesas
* Dashboard com o saldo atual de cada conta

<h2>🛠️ Como rodar o projeto:</h2>

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
  
<h2>💻 Desenvolvido com</h2>

Tecnologias utilizadas no projeto:

*   Python v3.10.8
*   alembic v1.10.2
*   attrs v22.2.0
*   Authlib v1.2.0
*   Babel v2.12.1
*   bcrypt v4.0.1
*   blinker v1.5
*   Bootstrap-Flask v2.2.0
*   cachetools v5.3.0
*   certifi v2022.12.7
*   cffi v1.15.1
*   charset-normalizer v3.1.0
*   click v8.1.3
*   colorama v0.4.6
*   cryptography v40.0.1
*   dnspython v2.3.0
*   dominate v2.7.0
*   email-validator v1.3.1
*   exceptiongroup v1.1.1
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
*   google-auth v2.16.3
*   google-auth-oauthlib v1.0.0
*   greenlet v2.0.2
*   gunicorn v20.1.0
*   idna v3.4
*   iniconfig v2.0.0
*   itsdangerous v2.1.2
*   Jinja2 v3.1.2
*   Mako v1.2.4
*   MarkupSafe v2.1.2
*   oauthlib v3.2.2
*   packaging v23.0
*   pathlib v1.0.1
*   pip v23.0.1
*   pluggy v1.0.0
*   pyasn1 v0.4.8
*   pyasn1-modules v0.2.8
*   pycparser v2.21
*   pytest v7.2.2
*   python-dotenv v1.0.0
*   pytz v2022.7.1
*   requests v2.28.2
*   requests-oauthlib v1.3.1
*   rsa v4.9
*   setuptools v67.4.0
*   six v1.16.0
*   SQLAlchemy v2.0.7
*   tomli v2.0.1
*   typing\_extensions v4.5.0
*   urllib3 v1.26.15
*   visitor v0.1.3
*   Werkzeug v2.2.3
*   wheel v0.38.4
*   WTForms v3.0.1

🍰 Como contribuir:
Caso queira contribuir com o projeto sinta-se à vontade para abrir uma issue ou enviar um pull request.

<h2>🛡️ Licença:</h2>

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.