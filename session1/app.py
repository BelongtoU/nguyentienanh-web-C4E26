from flask import Flask
app = Flask(__name__)

#bind route to view function
@app.route('/') #route
def home():     # view function
    return 'Hello C4E, hihi !!!'


@app.route("/myclass")
def myclass():
    return "asdfghj"

@app.route("/<name>")
def duc(name):
    return "hi " + name

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    return str(int(num1) + int(num2))

if __name__ == '__main__':
  app.run(debug=True)


