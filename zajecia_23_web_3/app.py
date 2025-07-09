from flask import Flask, render_template, request, redirect


users = [
    {
        "name": "Alice",
        "age": 30,
        "email": "alice_example.com",
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 25,
        "email": "bob_example.com",
        "city": "Los Angeles"
    },
    {
        "name": "Charlie",
        "age": 35,
        "email": "charlie_example.com",
        "city": "Chicago"
    }
]

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

@app.route("/")
def hello():
    return render_template("hello_world.html")

@app.route("/hello")
@app.route("/hello/<name>")
def hello_user(name=None):
    return render_template("hello_user.html", user_name=name, user_age=100)


@app.route("/users", methods=["GET", "POST"])
def show_users():
    if request.method == "POST":
        new_user = {
            "name": request.form.get("name"),
            "age": request.form.get("age"),
            "email": request.form.get("email"),
            "city": request.form.get("city_name")
        }
        users.append(new_user)
        return redirect("/")
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
