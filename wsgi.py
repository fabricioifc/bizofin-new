from app import create_app

app = create_app()

with app.app_context():
    from app.extensions import db

    # print('Excluindo tabelas')
    # db.drop_all()
    print('Criando tabelas')
    db.create_all()