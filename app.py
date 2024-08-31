from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/addition")
def addition_page():
    return render_template("addition.html")

@app.route("/subtraction")
def subtraction_page():
    return render_template("subtraction.html")

@app.route("/multiplication")
def multication_page():
    return render_template("multiplication.html")

@app.route("/division")
def division_page():
    return render_template("division.html")

@app.route("/placevalues")
def place_values_page():
    return render_template("place_values.html")

@app.route("/decimals")
def decimals_page():
    return render_template("decimals.html")

@app.route("/fractionsandpercentages")
def fractions_percentages_page():
    return render_template("fractions.html")

@app.route("/time")
def time_page():
    return "<h1>Time Page</h1>"

@app.route("/money")
def money_page():
    return "<h1>Money Page</h1>"

if __name__ == "__main__":

    # To test on this computer only
    #app.run(debug=True)

    # To test on another computer
    app.run(debug=True, host='0.0.0.0')