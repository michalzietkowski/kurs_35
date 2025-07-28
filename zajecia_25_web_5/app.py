from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zajecia_25_baza.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, server_default='dummy.email@gmail.com')

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name})"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




with app.app_context():
    db.create_all() # Tworzenie tabel w bazie danych
    ### OPERACJA TWORZENIA NOWEGO REKORDU W BAZIE DANYCH
    # user = User(
    #     username='admin2',
    #     password='admin123',
    #     first_name='Admin',
    #     last_name='User'
    # )
    # db.session.add(user) # Dodanie użytkownika do bazy danych
    # db.session.commit() # Zapisanie zmian w bazie danych
    # admin_3 = User(
    #     username="admin_3",
    #     password="admin123",
    #     first_name="Admin",
    #     last_name="User",
    #     email="admin_3@gmail.com",
    # )
    # db.session.add(admin_3)  # Dodanie użytkownika do bazy danych
    # db.session.commit()  # Zapisanie zmian w bazie danych

    ### OPERACJA ODCZYTU REKORDÓW Z BAZY DANYCH
    # users = User.query.all()
    # print(users)
    # first_user = User.query.first()
    # print(first_user)
    # admin_2 = User.query.filter_by(first_name="Admin", last_name="User").all()
    # print(admin_2)

    ### OPERACJA ZMIANY REKORDÓW W BAZIE DANYCH
    # admin_2_to_change = User.query.filter_by(username="admin2").first()
    # admin_2_to_change.last_name = "Admin"
    # db.session.add(admin_2_to_change)
    # db.session.commit() # Zapisanie zmian w bazie danych

    ### OPERACJA USUWANIA REKORDÓW Z BAZY DANYCH
    # db.session.delete(admin_2_to_change) # Usunięcie użytkownika z bazy danych
    # db.session.commit() # Zapisanie zmian w bazie danych
    # data_to_remove = User.query.filter_by(username="admin").delete()
    # db.session.commit() # Zapisanie zmian w bazie danych

if __name__ == '__main__':
    app.run(debug=True) # Uruchomienie aplikacji Flask w trybie debugowania