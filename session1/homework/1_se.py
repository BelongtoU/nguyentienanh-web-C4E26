from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Please add in address url with format: "/bmi/<your_ weight>(in kg)/<height>(in centimeter)" to calculate your BMI =)) hihi !!!'

# # without render_template() function
# @app.route("/bmi/<weight>/<height>")
# def bmi (weight, height):
#     w = float(weight)
#     h = int(height)

#     bmi_id = w/(h*h/10000) 

#     if bmi_id < 16:
#         return "Your BMI = {} => Severely underweight !!!".format(bmi_id)
#     elif bmi_id < 18.5:
#         return "Your BMI = {} => Underweight !".format(bmi_id)
#     elif bmi_id < 25:
#         return "Your BMI = {} => Normal <3".format(bmi_id)
#     elif bmi_id < 30:
#         return "Your BMI = {} => Overweight !".format(bmi_id)
#     else:
#         return "Your BMI = {} => Obese !!!".format(bmi_id)


# with render_template() function
@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi_id = weight/(height*height/10000)

    s_u = bmi_id < 16
    u = 16 <= bmi_id < 18.5
    n = 18.5 <= bmi_id < 25 
    o = 25 <= bmi_id < 30
    ob = 30 < bmi_id 

    l = [
      {
        "key": s_u,
        "value": "Severely underweight !!!"
      },
      {
        "key": u,
        "value": "Underweight !"
      },
      {
        "key": n,
        "value": "Normal <3"
      },
      {
        "key": o,
        "value": "Overweight !"
      },
      {
        "key": ob,
        "value": "Obese !!!"
      },
    ]
    return render_template("bmi.html", st_l = l, bmi = bmi_id)

if __name__ == '__main__':
  app.run(debug=True)