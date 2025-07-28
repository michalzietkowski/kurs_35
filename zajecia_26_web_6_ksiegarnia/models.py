from flask_sqlalchemy import SQLAlchemy

# Tworzymy instancję db bez aplikacji
db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    amount_available = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)