from flask import Flask, render_template, redirect

t_anh = Flask(__name__)

@t_anh.route('/')
def home():
    return 'Hello, Please add "/about-me" in adress url to get some personal infomations about me =)) hihi !!!'

@t_anh.route("/about-me")
def me ():
  abm_l = [
    {
      "key": "Full name",
      "value": "Nguyễn Tiến Anh"
    },
    {
      "key": "Date of birth",
      "value": "09-11-1998"
    },
    {
      "key": "Location",
      "value": "Liên Bạt - Ứng Hòa - Hà Nội"
    },
    {
      "key": "Hobbies",
      "value": "Soccer, Reading, Cooking, ... or st like creating st new =))"
    }
  ]

  return render_template("about_me.html", ab_m = abm_l) 


@t_anh.route("/school")
def tk():
  return redirect("http://techkids.vn")

if __name__ == '__main__':
  t_anh.run(debug=True)