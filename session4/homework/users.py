from flask import Flask, render_template, request, redirect
import functions
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("users.html")

passwords = "ourtownsobeautiful"
@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    form = request.form
    if functions.check_acc(form["user"]):
      if form["pass"] == passwords:
        return render_template("lienbat.html")
      else:
        return render_template("notice_wrong.html")

@app.route("/lienbat")
def lienbat():
  return "hello"

if __name__ == '__main__':
  app.run(debug=True)