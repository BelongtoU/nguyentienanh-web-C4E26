from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, add in the address url: /new_bike to add a bike to your rental bike list =)) hihi !!!'

rental_bikes =[]

@app.route("/new_bike", methods = ["GET", "POST"])
def n_b ():
  if request.method == "GET":
    return render_template("bike_rental_service.html")
  elif request.method =="POST":
    form_full = request.form 
    new_bikes = {
      "Model": form_full["model"],
      "Fee": form_full["fee"],
      "Img": form_full["img"],
      "Year": form_full["year"]
    }
    rental_bikes.append(new_bikes)
    print(new_bikes)        #ex_3
    return "A new bike is added in list"


if __name__ == '__main__':
  app.run(debug=True)