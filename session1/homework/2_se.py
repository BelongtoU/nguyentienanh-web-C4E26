from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, add to the address url follow form: '/user/user_name' to get some user profile =)) hihi. But now, you only can enter user_names: huy, tienanh, mai :(("

@app.route("/user/<username>")
def user_prf (username):
    users = {
        "huy": {
            "name": "Nguyen Quang Huy",
            "age": 29,
        },
        "tienanh": {
            "name": "Nguyen Tien Anh",
            "age": 21,
        },
        "mai": {
            "name": "Nguyen Thi Mai",
            "age": 17,
        },
    }

    if username in users.keys() :
        return render_template("user.html", name = users[username]["name"], age = users[username]["age"] )
    else:
        return "USER NOT FOUND, PLZ CHECK AGAIN !!!"    

if __name__ == '__main__':
  app.run(debug=True)
