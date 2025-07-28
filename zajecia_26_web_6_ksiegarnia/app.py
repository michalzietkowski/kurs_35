from flask import Flask

def create_app():
    """Application factory function"""
    app = Flask(__name__)
    app.secret_key = 'ksiegarnia_secret_key_2024'  # Wymagane dla flash messages
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ksiegarnia.db'

    # Inicjalizujemy db z aplikacją
    from models import db
    db.init_app(app)
    
    # Rejestrujemy blueprint
    from routes import ksiegarnia_blueprint
    app.register_blueprint(ksiegarnia_blueprint)
    
    # Tworzymy tabele w kontekście aplikacji
    with app.app_context():
        from models import Saldo
        db.create_all()  # Tworzy tabele w bazie danych, jeśli nie istnieją
        saldo = db.session.query(Saldo).first()
        if not saldo:
            # Jeśli saldo nie istnieje, tworzymy domyślne saldo
            default_saldo = Saldo(amount=10000.0)
            db.session.add(default_saldo)
            db.session.commit()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)