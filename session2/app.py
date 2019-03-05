from flask import Flask, render_template, request
app = Flask(__name__)

items = [
    {
        "name": "com rang",
        "price": "25 000" 
    },
    {
        "name": "pho bo",
        "price": "30 000" 
    },
    {
        "name": "bun ca",
        "price": "50 000" 
    }, 
]

@app.route("/")
def menu():
    return render_template("menu.html", items_l = items, user = "N T.Anh")

@app.route('/menu/<int:id>')
def menu_detail (id):
    return render_template("food_detail.html", items_l = items[id])

@app.route("/add_food", methods = ["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form 
        n = form["name"]
        p = form["price"]
        new_item = {
            "name": n,
            "price": p
        }
        items.append(new_item)
        return n + " created sucessfully !!!"

if __name__ == '__main__':
  app.run(debug=True)