from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="John Hayes"
role="Systems Administrator"
phone="773.430.4461"
email="jahayesjr.37@gmail.com"
location="Murfreesboro, Tennessee, United States"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email
    )

if __name__ == "__main__":
    app.run(debug=True)
