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
    saldo = 10
    if request.method == "POST":
        form_type = request.form.get("form_type")
        match form_type:
            case "change_price":
                print("Changing price")
                saldo = request.form.get("new_saldo")
            case "add_user":
                print(form_type)
                new_user = {
                    "name": request.form.get("name"),
                    "age": request.form.get("age"),
                    "email": request.form.get("email"),
                    "city": request.form.get("city_name")
                }
                users.append(new_user)

            case "delete_user":
                print(form_type)
                user_name = request.form.get("delete_name")
                for user in users:
                    if user["name"] == user_name:
                        users.remove(user)
                        break
    return render_template("users.html", users=users, saldo=saldo)


if __name__ == "__main__":
    app.run(debug=True)
