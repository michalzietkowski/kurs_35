from flask import Flask
from routes import ksiegarnia_blueprint

app = Flask(__name__)
app.secret_key = 'ksiegarnia_secret_key_2024'  # Wymagane dla flash messages
app.register_blueprint(ksiegarnia_blueprint)

if __name__ == '__main__':
    app.run(debug=True)