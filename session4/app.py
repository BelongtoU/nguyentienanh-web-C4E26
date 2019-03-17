from flask import Flask, render_template
import food 

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello C4E, hihi !!!'

@app.route("/food_list")
def food_list():
  food_l = food.get({})
  return render_template("food_list.html", fl = food_l)

@app.route("/food/<id>")
def food_detail(id):
  f = food.get_by_id(id)
  return f['name']



if __name__ == '__main__':
  app.run(debug=True)