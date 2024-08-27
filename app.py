from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Home Page</h1>"

@app.route("/addition")
def addition_page():
    return "<h1>Addition Page</h1>"

@app.route("/subtraction")
def subtraction_page():
    return "<h1>Subtraction Page</h1>"

@app.route("/multiplication")
def multication_page():
    return "<h1>Multiplication Page</h1>"

@app.route("/division")
def division_page():
    return "<h1>Division Page</h1>"

@app.route("/placevalues")
def place_values_page():
    return "<h1>Place Values Page</h1>"

@app.route("/decimals")
def decimals_page():
    return "<h1>Decimals Page</h1>"

@app.route("/fractionsandpercentages")
def fractions_percentages_page():
    return "<h1>Fractions and Percentages Page</h1>"

@app.route("/time")
def time_page():
    return "<h1>Time Page</h1>"

@app.route("/money")
def money_page():
    return "<h1>Money Page</h1>"

if __name__ == "__main__":

    # To test on this computer only
    app.run(debug=True)

    # To test on another computer
    #app.run(debug=True, host='0.0.0.0')