from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, This is some infomations about me =)) hihi !!!'

@app.route("/about-me")
def me ():
    l1 = "Name: Nguyen Tien Anh\n"
    l2 = "Date of birth: 09-11-1998"
    a = l1 + l2
    return  a


if __name__ == '__main__':
  app.run(debug=True)