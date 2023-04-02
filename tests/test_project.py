from app.models import User
from flask import session

def test_home(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b"<h3>P\xc3\xa1gina Inicial</h3>" in response.data


def test_registration(client, app):
    response = client.post('/accounts/register', data={"email": "teste@teste.com", "password": "123456", "confirm": "123456"}, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "teste@teste.com"
        # assert b"<h3>Cadastro de Usu\xc3\xa1rio</h3>" in response.data

def test_login_valido(client):
    client.post('/accounts/register', data={"email": "teste@teste.com", "password": "123456", "confirm": "123456"})
    client.post('/accounts/login', data={"email": "teste@teste.com", "password": "123456"})

    response = client.get('/contas', follow_redirects=True)

    assert "Você se registrou e agora está logado. Bem-vindo!" in response.data.decode('utf-8')

def test_login_invalido(client):
    client.post('/accounts/login', data={"email": "teste@teste.com", "password": "123456"})

    response = client.get('/contas', follow_redirects=True)
    assert "Por favor, faça o login para acessar esta página." in response.data.decode('utf-8')

def test_login_valido_user(client):
    client.post('/accounts/register', data={"email": "teste@teste.com", "password": "123456", "confirm": "123456"})
    client.get('/accounts/logout', follow_redirects=True)
    response = client.post('/accounts/login', data={"email": "teste@teste.com.br", "password": "654321"}, follow_redirects=True)

    assert "Nome de usuário ou senha inválidos!" in response.data.decode('utf-8')